import os
import sys

# التأكد من تشغيل السكربت من داخل مجلد SmartClinic_Docs
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# استيراد البيانات من ملف content/data.py
sys.path.append(current_dir)
try:
    from content.data import PAGES_DATA
except ImportError as e:
    print(f"❌ خطأ: تعذر العثور على ملف البيانات content/data.py\n{e}")
    sys.exit(1)

def build_site():
    print("🚀 بدء توليد موقع التوثيق الثابت...")
    
    # التأكد من وجود القالب الأساسي
    template_path = os.path.join("template", "base.html")
    if not os.path.exists(template_path):
        print("❌ خطأ: قالب التصميم template/base.html غير موجود.")
        sys.exit(1)
        
    with open(template_path, "r", encoding="utf-8") as f:
        base_html = f.read()

    # ── 1. توليد شريط التنقل الجانبي (Sidebar Links) ──
    nav_links_html = ""
    for page_id, data in PAGES_DATA.items():
        icon = data.get("icon", "bi-file-earmark-text")
        title = data.get("nav_title", data["title"])
        # سيتم استبدال {active_class} لاحقاً لكل صفحة على حدة
        link = f'''
        <a href="{page_id}.html" class="nav-btn {{active_{page_id}}}">
            <i class="bi {icon}"></i> {title}
        </a>'''
        nav_links_html += link

    # ── 2. توليد الصفحات المستقلة ──
    generated_count = 0
    for page_id, data in PAGES_DATA.items():
        # تجهيز شريط التنقل الخاص بهذه الصفحة (تفعيل الزر الحالي)
        current_nav = nav_links_html
        for p_id in PAGES_DATA.keys():
            replacement = "active" if p_id == page_id else ""
            current_nav = current_nav.replace(f"{{active_{p_id}}}", replacement)
        
        # دمج البيانات في القالب
        page_html = base_html
        page_html = page_html.replace("{{ title }}", data["title"])
        page_html = page_html.replace("{{ description }}", data["description"])
        page_html = page_html.replace("{{ content }}", data["content"])
        page_html = page_html.replace("{{ nav_links }}", current_nav)
        
        # حفظ الملف في المجلد الرئيسي للتوثيق
        output_path = os.path.join(current_dir, f"{page_id}.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(page_html)
            
        print(f"✅ تم توليد: {page_id}.html")
        generated_count += 1
        
    print(f"🎉 اكتمل بنجاح! تم بناء {generated_count} صفحات.")
    print(f"👉 يمكنك الآن فتح ملف index.html في المتصفح لرؤية التوثيق المذهل.")

if __name__ == "__main__":
    build_site()
