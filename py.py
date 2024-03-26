import tkinter as tk

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("اهلا")
window.geometry("300x200")

# إنشاء عنصر النص
label = tk.Label(window, text="  مرحبا ")
label.pack()

# تشغيل الحلقة الرئيسية للتطبيق
window.mainloop()