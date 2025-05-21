from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import pickle
from datetime import datetime
import logging

# 設置日誌
logger = logging.getLogger(__name__)

# 如果修改這些範圍，請刪除 token.pickle 文件
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# 默認的 Google Drive 文件夾 ID
DEFAULT_FOLDER_ID = "1f-V5UXwwhVfs-Qj_Uu8MU05FXe_MWP_0"  # 請替換為您的實際文件夾ID

def get_google_drive_service():
    """獲取 Google Drive 服務實例"""
    creds = None
    # token.pickle 文件存儲用戶的訪問和刷新令牌
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # 如果沒有有效的憑證，讓用戶登錄
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', 
                SCOPES,
                redirect_uri='http://localhost:8000/oauth2callback'  # 添加重定向 URI
            )
            creds = flow.run_local_server(port=0)
        # 保存憑證以供下次使用
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

def upload_image_to_drive(file_path, folder_id=DEFAULT_FOLDER_ID):
    """
    上傳圖片到 Google Drive
    
    Args:
        file_path (str): 本地圖片文件路徑
        folder_id (str, optional): Google Drive 文件夾 ID，默認為 DEFAULT_FOLDER_ID
    
    Returns:
        str: 公開訪問的圖片 URL
    """
    try:
        service = get_google_drive_service()
        
        # 生成文件名
        file_name = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.path.basename(file_path)}"
        
        # 創建文件元數據
        file_metadata = {
            'name': file_name,
            'mimeType': 'image/jpeg'
        }
        
        if folder_id:
            file_metadata['parents'] = [folder_id]
        
        # 創建媒體文件上傳對象
        media = MediaFileUpload(
            file_path,
            mimetype='image/jpeg',
            resumable=True
        )
        
        # 上傳文件
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        # 設置文件權限為公開
        service.permissions().create(
            fileId=file.get('id'),
            body={'type': 'anyone', 'role': 'reader'}
        ).execute()
        
        # 獲取公開 URL
        file = service.files().get(
            fileId=file.get('id'),
            fields='webViewLink, webContentLink'
        ).execute()
        
        logger.info(f"圖片已成功上傳到 Google Drive，URL: {file.get('webContentLink')}")
        return file.get('webContentLink')
        
    except Exception as e:
        logger.error(f"上傳圖片到 Google Drive 時發生錯誤: {str(e)}")
        raise 