import { describe, it, expect, vi, beforeEach } from "vitest";
import { mount } from "@vue/test-utils";
import CreateTodo from "../src/components/CreateTodo.vue"; // ← 改這裡

describe("CreateTodo.vue", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("輸入框可以綁定資料（v-model）", async () => {
    const wrapper = mount(CreateTodo); // ← 改這裡
    const input = wrapper.find("input");
    await input.setValue("New Task");
    expect(wrapper.vm.name).toBe("New Task");
  });

  it("按下按鈕會觸發 fetch 並清空輸入", async () => {
    global.fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({}),
      })
    );

    const wrapper = mount(CreateTodo); // ← 改這裡
    await wrapper.find("input").setValue("Mocked Task");
    await wrapper.find("button").trigger("click");

    expect(global.fetch).toHaveBeenCalled();
    expect(wrapper.vm.name).toBe("");
  });
});
