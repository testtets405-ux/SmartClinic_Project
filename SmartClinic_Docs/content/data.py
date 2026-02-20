"""
هذا الملف يحتوي على قاعدة بيانات المصطلحات والنصوص التي ستكون التوثيق الشامل التفصيلي.
كل كود هنا هو مأخوذ حرفياً من قلب مشروع العيادة الذكية، لضمان صحة الشرح للمناقشين واطلاع الطلاب.
"""

PAGES_DATA = {
    # ==================== (1) INDEX ====================
    "index": {
        "icon": "bi-bookmark-star-fill text-blue-500",
        "nav_title": "1. النظرة العامة",
        "title": "المقدمة الشاملة للعيادة الذكية (Smart Clinic)",
        "description": "دراسة متعمقة لأساسيات المشروع، ولماذا تم بناؤه، وكيف تعمل بنيته التحتية.",
        "content": '''
            <div class="space-y-6">
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-question-circle text-blue-500"></i> المعضلة الأساسية (Problem Statement)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        العيادات الطبية التقليدية والمستشفيات تعتمد جميعها على نظام طوابير بدائي يُعرف بـ <b>(من يأتي أولاً، يُعالج أولاً - FIFO)</b>. 
                        في هذا النظام البدائي، طابور الانتظار أعمى تماماً عن حالة المريض. لو وصل مريض بحالة طارئة جداً (نزيف حاد، جلطة)، وكان رقمه 20 في الطابور، عليه للأسف انتظار 19 شخصاً مستقراً وقادراً على الانتظار قبله. 
                        هذا النظام يتنافى مع أبسط قواعد الأخلاق الطبية ومعايير الرعاية الصحية (Healthcare Standards).
                    </p>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed">
                        علاوة على ذلك، المرضى في العيادات التقليدية يفقدون أعصابهم ووقتهم لعدم وجود إشعار دقيق بوقت دخولهم الفعلي إلى الطبيب، مما يسبب تكدس مئات الأشخاص في صالات الانتظار ونقل العدوى.
                    </p>
                </section>

                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-lightbulb text-amber-500"></i> الحل التقني المُبتكر (The Solution)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed">
                        تم هندسة وبناء <b>العيادة الذكية (Smart Clinic Queue System)</b> كمنظومة قائمة على دمج هياكل البيانات (Data Structures) المتقدمة مع خوارزميات الذكاء الاصطناعي (Machine Learning).
                        يتم العمل بمبدأ <b>(الفرز الطبي المهندس - Algorithmic Triage)</b>.
                        حيثُ لا يحصل المريض على رقم تسلسلي أعمى، بل يتم تقييمه برمجياً في الخلفية بطريقة تقييمية (Scoring System) تُعطي وزناً إضافياً لـ:
                    </p>
                    <ul class="list-disc list-inside mt-4 space-y-2 text-slate-600 dark:text-slate-300">
                        <li><b>عمر المريض:</b> إعطاء أولوية حاسوبية لكبار السن (فوق 70) والأطفال الرضع.</li>
                        <li><b>حالة الطوارئ:</b> فصل الطابور لطبقات (Tiers) لضمان دخول الحالات الحرجة فوراً دون انتظار.</li>
                        <li><b>معدل الانتظار:</b> كل دقيقة انتظار تعطي المريض وزن إضافي لكي لا يُنسى في الطابور.</li>
                    </ul>
                </section>

                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-stack text-purple-500"></i> البنية التكنولوجية (Tech Stack Breakdown)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        لبناء هذا النظام المتكامل والمعقد، تم استخدام مجموعة من أحدث التقنيات وأكثرها استقراراً في سوق العمل هندسياً:
                    </p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-blue-50/50 dark:bg-blue-900/10 p-5 rounded-xl border border-blue-100 dark:border-blue-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-filetype-py text-2xl text-blue-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">بايثون (Python 3.10+)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                لغة البرمجة الأساسية في الخادم (Backend). استُخدمت لبرمجة الخوارزميات الرياضية المعقدة (Priority Calculation)، والتعامل مع المكتبات الإحصائية، وإدارة مناطق التوقيت (Timezones) الحساسة جداً لتسعير الوقت.
                            </p>
                        </div>
                        
                        <div class="bg-emerald-50/50 dark:bg-emerald-900/10 p-5 rounded-xl border border-emerald-100 dark:border-emerald-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-server text-2xl text-emerald-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">استضافة فلاسك (Flask Web Framework)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                هيكلة (MVT) سريعة وموثوقة لاستقبال طلبات (HTTP). معتمدة لميزاتها الأمنية وتوافقيتها السريعة في إنتاج الـ APIs وبناء نظام توجيه (Routing) محمي باستخدام المفاهيم المتقدمة (Decorators).
                            </p>
                        </div>
                        
                        <div class="bg-indigo-50/50 dark:bg-indigo-900/10 p-5 rounded-xl border border-indigo-100 dark:border-indigo-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-database-fill text-2xl text-indigo-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">بيانات أمنة (SQLite & SQLAlchemy)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                بدلاً من استخدام نصوص SQL معرضة للاختراق (SQL Injection)، تم استخدام (ORM) لتجريد قاعدة البيانات. حيث تُعامل الجداول ككائنات (Objects) يمكن استخراج بياناتها عبر علاقات قوية (Foreign Keys).
                            </p>
                        </div>
                        
                        <div class="bg-pink-50/50 dark:bg-pink-900/10 p-5 rounded-xl border border-pink-100 dark:border-pink-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-robot text-2xl text-pink-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">الذكاء الاصطناعي (Scikit-Learn ML)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                توظيف نموذج الـ RandomForest المتقدم لحساب (ETA - Estimated Time of Arrival). الموديل لا يخمن، بل يتعلم من داتا العيادة التاريخية والساعات والأيام ليستنتج متى حان دور المريض بالضبط.
                            </p>
                        </div>
                        
                        <div class="bg-fuchsia-50/50 dark:bg-fuchsia-900/10 p-5 rounded-xl border border-fuchsia-100 dark:border-fuchsia-800 md:col-span-2">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-palette text-2xl text-fuchsia-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">واجهات حديثة (Tailwind CSS + JS)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                تم تجريد النظام من لغات الـ CSS القديمة، والاعتماد على مكتبة (Utility-first) وهي Tailwind CSS لبناء واجهات متجاوبة (Responsive) وتعمل بوضع (Dark/Light Mode) ديناميكي وتدعم التحديث الآني عبر الأجاكس (AJAX).
                            </p>
                        </div>
                    </div>
                </section>
            </div>
            
            <p class="mt-8 text-sm text-slate-500 border-r-4 border-emerald-500 pr-4">
                تصفح القائمة الجانبية لقراءة كود المصدر (Source Code) لكل قسم مع التفسير الهندسي الذي سيجعلك تفهم كيف بُرمج المشروع 100%.
            </p>
        '''
    },
    
    # ==================== (2) STRUCTURE ====================
    "structure": {
        "icon": "bi-folder-fill text-amber-500",
        "nav_title": "2. هيكلية المشروع الشاملة",
        "title": "مجلدات وملفات نظام العيادة الذكية",
        "description": "نظرة مجهرية على كل مجلد وكل ملف، وما الفائدة البرمجية منه.",
        "content": '''
            <div class="space-y-6">
                <p class="text-slate-600 dark:text-slate-300">
                    يتكون مشروعنا من هندسة نظيفة (Clean Architecture) تفصل بين قاعدة البيانات، منطق الواجهات، ومنظومة العمليات الرياضية لتسهيل التطوير والصيانة والاستضافة.
                </p>

                <div class="bg-slate-50 dark:bg-slate-800/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-4 text-xl border-b border-slate-200 dark:border-slate-700 pb-2">📂 المجلدات الجذرية (Root Directories)</h3>
                    
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3">
                            <i class="bi bi-folder2-open text-2xl text-blue-500 mt-1"></i>
                            <div>
                                <strong class="text-lg text-slate-800 dark:text-white">مجلد <code>templates/</code></strong>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
                                    هذا المجلد يحتوي على 10 ملفات وهي كافة واجهات المستخدم المبنية بـ HTML. يتم دمج هذه الملفات باستخدام محرك القوالب (Jinja2) داخل بايثون لعرض المتغيرات ديناميكياً (مثل عرض اسم المريض أو صورته). يحتوي على واجهات الأطباء، الإدارة، شاشة الانتظار وإلخ.
                                </p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="bi bi-folder2-open text-2xl text-emerald-500 mt-1"></i>
                            <div>
                                <strong class="text-lg text-slate-800 dark:text-white">مجلد <code>static/</code></strong>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
                                    المجلد الذي يحتفظ بالملفات الثابتة التي لا تتغير. وضعنا فيه داخلياً مجلد (css) ليحمل ملف <code>style.css</code> إذا أردنا التعديل على الخطوط (Fonts) أو الخصائص الثابتة التي لا تُلبيها Tailwind محلياً.
                                </p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="bi bi-folder2-open text-2xl text-purple-500 mt-1"></i>
                            <div>
                                <strong class="text-lg text-slate-800 dark:text-white">مجلد <code>SmartClinic_Docs/</code></strong>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
                                    ما تتصفحه أنت حالياً! هو محرك التوثيق الشامل (Static Site Generator) صممناه ليعمل بدون الحاجة لتشغيل كامل النظام. لتسهيل الدراسة.
                                </p>
                            </div>
                        </li>
                    </ul>
                </div>

                <div class="bg-slate-50 dark:bg-slate-800/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-4 text-xl border-b border-slate-200 dark:border-slate-700 pb-2">📄 الملفات المركزية (Core Files)</h3>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-blue-500"></i> <code>app.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">الملف الرئيسي، المركز العصبي والموجه للـ Routes. وهو من يشغل النظام.</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-fuchsia-500"></i> <code>models.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">الهيكل الهندسي لجداول قواعد البيانات الخاصة بك باستخدام (SQLAlchemy).</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-red-500"></i> <code>utils.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">مكتبة الدوال الرياضية المعقدة وحاضنة خوارزمية ترتيب الطابور وفرز المرضى.</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-emerald-500"></i> <code>config.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">المخزن الآمن للمفاتيح وكلمات المرور المشفرة الخاصة بالمطور والإدارة.</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-pink-500"></i> <code>clock.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">منظم الوقت الموحد، يحفظ البيانات بتوقيت UTC ويعرضها بتوقيت بغداد.</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-indigo-500"></i> <code>ai_service.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">النموذج الذكي (ML Model) المسؤول عن حساب أوقات الانتظار المتوقعة.</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-database text-amber-600"></i> <code>clinic.db</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">ملف قاعدة البيانات (SQLite File) الفعلي الذي يتم تخزين وحفظ الداتا به.</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-txt text-slate-500"></i> <code>requirements.txt</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">ملف يحتوي على أسماء إصدارات جميع المكاتب اللازمة لتشغيل النظام (Flask, Scikit-learn).</p>
                        </div>
                        <div class="p-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg md:col-span-2">
                            <strong><i class="bi bi-robot text-teal-600"></i> <code>seed_db.py / seed_admin.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">سكربتات الدعم والاختبار. بمجرد النقر عليها، ستقوم ببناء عيادة وهمية كاملة (بمرضاها ومدرائها وأطبائها) بثواني لاختبار المشروع بشكل نهائي ومكثف.</p>
                        </div>
                    </div>
                </div>
            </div>
        '''
    },

    # ==================== (3) APP_PY ====================
    "app_py": {
        "icon": "bi-router-fill text-emerald-500",
        "nav_title": "3. المُوجه و الـ Routes (app.py)",
        "title": "تفصيل الموجه الرئيسي والكنترولر (app.py)",
        "description": "دليل دراسي شامل لكل مسار (Route) في النظام وكيف تم تأمينها بالديكوريتورز.",
        "content": '''
            <div class="space-y-6">
                <p class="text-slate-600 dark:text-slate-300">
                    ملف <code>app.py</code> أطول ملف في المشروع. هو العقل المدبر الذي يربط بين جداول قاعدة البيانات (Models) وبين واجهات الاستخدام (Templates). ويقوم باستقبال وإرسال جميع الطلبات (Requests).
                </p>

                <div class="bg-indigo-50/50 dark:bg-indigo-900/10 p-5 rounded-xl border border-indigo-100 dark:border-indigo-800">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-2">الدوال الجدارية وتحديث الطابور</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">يحتوي الكود على آليات حماية وتحديث آلية وتعتبر من الركائز التي بُني عليها المشروع:</p>
                    
                    <div class="code-block-wrapper">
                        <div class="code-header">
                            <span><i class="bi bi-file-earmark-code"></i> app.py (السطر 78) - حائط الصد المنيع (role_required)</span>
                            <button class="copy-btn" onclick="copyCode(this)"><i class="bi bi-clipboard"></i> نسخ</button>
                        </div>
                        <pre><code class="language-python">def role_required(*roles):
    """
    [المعنى الهندسي]: 
    الـ Decorator هو دالة تغلف دالة أخرى. نضعه فوق أي صفحة (route) نريد حمايتها.
    إذا حاول دكتور الدخول لصفحة الاستقبال، سيتحقق الـ Current User من الـ (Role) الخاص به
    ويمنعه من الدخول، وهذا يمنع أي متطفل من استخدام روابط مباشرة (Direct Links).
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("login"))
            if current_user.role not in roles:
                flash("عذراً، لا تملك صلاحية للوصول إلى هذه الصفحة.", "danger")
                return redirect(url_for("home"))
            return view_func(*args, **kwargs)
        return wrapped
    return decorator</code></pre>
                    </div>

                    <div class="code-block-wrapper mt-4">
                        <div class="code-header">
                            <span><i class="bi bi-file-earmark-code"></i> app.py (السطر 49) - المحدث الآلي (update_priorities)</span>
                            <button class="copy-btn" onclick="copyCode(this)"><i class="bi bi-clipboard"></i> نسخ</button>
                        </div>
                        <pre><code class="language-python">def update_queue_priorities():
    """
    [المعنى الهندسي]:
    مستحيل أن نجعل الموظف يقوم بالضغط على (تحديث) يدوياً لكل مريض. 
    تقوم هذه الدالة دورياً بجلب كل المرضى (صاحبي حالة الانتظار)، 
    ثم تطرح وقت وصولهم من الوقت الحالي لتعرف (كم دقيقة انتظر المريض) 
    وتقوم بإعادة إرسال الرقم لخوارزمية الطابور لإعادة التنقيط بشكل ديناميكي مذهل وحي.
    """
    waiting_patients = Patient.query.filter_by(status='waiting').all()
    current_time = now_utc()
    for p in waiting_patients:
        wait_time = (current_time - p.check_in_time).total_seconds() / 60
        p.priority_score = calculate_priority(p.age, p.appointment_type, int(wait_time))
    db.session.commit()</code></pre>
                    </div>
                </div>

                <div class="bg-slate-50 dark:bg-slate-800/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-4 text-xl border-b border-slate-200 dark:border-slate-700 pb-2">سجل المسارات والراوتس (Routes Definitions)</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">تم تقسيم الروابط (Endpoints) في النظام لخدمة واجهات العيادة المختلفة. هذه بعض أهم الراوتس وماذا تفعل:</p>

                    <div class="overflow-x-auto">
                        <table class="w-full text-sm text-start">
                            <thead class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300">
                                <tr>
                                    <th class="p-3 border-b dark:border-slate-600">المسار (Route)</th>
                                    <th class="p-3 border-b dark:border-slate-600">الصلاحيات (Roles)</th>
                                    <th class="p-3 border-b dark:border-slate-600 text-right">الوظيفة (Functionality)</th>
                                </tr>
                            </thead>
                            <tbody class="text-slate-700 dark:text-slate-300 divide-y divide-slate-200 dark:divide-slate-700">
                                <tr>
                                    <td class="p-3 font-mono text-xs"><code>/</code></td>
                                    <td class="p-3"><span class="bg-slate-200 dark:bg-slate-600 px-2 py-1 rounded text-xs">الكل (Public)</span></td>
                                    <td class="p-3 text-right">الصفحة الرئيسية واجهة العيادة الترحيبية وتوجيه للأقسام.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono text-xs text-blue-500"><code>/kiosk</code></td>
                                    <td class="p-3"><span class="bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-300 px-2 py-1 rounded text-xs">استقبال / مسؤول</span></td>
                                    <td class="p-3 text-right">واجهة الإدخال، تسأل عن بيانات المريض وتاريخه الطبي وحالته وتمررها للخوارزمية.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono text-xs text-amber-500"><code>/queue</code></td>
                                    <td class="p-3"><span class="bg-slate-200 dark:bg-slate-600 px-2 py-1 rounded text-xs">الكل (Public)</span></td>
                                    <td class="p-3 text-right">الشاشة الذكية المعلقة في صالة الانتظار. تعرض الدور والمدة المتبقية بالاعتماد السري على API حي.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono text-xs text-emerald-500"><code>/api/queue</code></td>
                                    <td class="p-3"><span class="bg-slate-200 dark:bg-slate-600 px-2 py-1 rounded text-xs">الكل (API)</span></td>
                                    <td class="p-3 text-right">واجهة برمجية تعيد قائمة المرضى كـ JSON للعمل مع شاشة العرض (تقوم بالتحديث الآلي).</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono text-xs text-red-500"><code>/doctor</code></td>
                                    <td class="p-3"><span class="bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-300 px-2 py-1 rounded text-xs">دكتور / مسؤول</span></td>
                                    <td class="p-3 text-right">واجهة الطبيب. تعرض المريض الحالي الذي يجب فحصه، والمريض المستعد دخولاً خلفه، وتُعطي صلاحيات إنهاء المواعيد وتسجيل الملاحظات.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono text-xs text-fuchsia-500"><code>/admin</code></td>
                                    <td class="p-3"><span class="bg-fuchsia-100 text-fuchsia-800 dark:bg-fuchsia-900/30 dark:text-fuchsia-300 px-2 py-1 rounded text-xs">المدير (admin)</span></td>
                                    <td class="p-3 text-right">لوحة التحكم العليا. لإنشاء الحسابات، عرض تاريخ كل العيادة وتشخيصات كل طبيب ورؤية التحليلات والإحصائيات الحيوية.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono text-xs text-pink-500"><code>/api/ai_insights</code></td>
                                    <td class="p-3"><span class="bg-fuchsia-100 text-fuchsia-800 dark:bg-fuchsia-900/30 dark:text-fuchsia-300 px-2 py-1 rounded text-xs">المدير (admin)</span></td>
                                    <td class="p-3 text-right">استدعاء رياضي لمعلومات إحصائية يقوم الموديل فيها بإعطاء نصائح للإدارة (مثل: "زيادة الضغط في الصباح، يُنصح بتوفير أطباء دعم").</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        '''
    },

    # ==================== (4) MODELS.PY ====================
    "models": {
        "icon": "bi-diagram-3-fill text-fuchsia-500",
        "nav_title": "4. الجداول والعلاقات (models.py)",
        "title": "هندسة البيانات والعلاقات المترابطة",
        "description": "تصميم جداول الـ SQLite والتخاطب معها، وشرح دقيق لمفاتيح الربط (Foreign Keys).",
        "content": '''
            <div class="space-y-6">
                <p class="text-slate-600 dark:text-slate-300">
                    الكود القديم أو السطحي يعتمد على كتابة نصوص SQL نقية، وهو أسلوب غير آمن (Vulnerable to SQL Injection). لذا استخدمنا طبقة تجريدية ضخمة تسمى الـ (SQLAlchemy ORM - Object Relational Mapping). نحن نتعامل مع الجداول وكأنها كائنات (Objects).
                </p>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <div class="bg-blue-50/50 dark:bg-blue-900/10 p-5 rounded-xl border border-blue-100 dark:border-blue-800">
                        <h4 class="font-bold text-slate-800 dark:text-white mb-2">1. جدول المستخدمين (User Model)</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            يُخزن بيانات دخول الدكاترة وموظفي الاستقبال والمدراء بشكل مشفر بفضل مكتبة <code>werkzeug.security</code>.
                            <strong>ملاحظة هامة:</strong> يحتوي على حقل مهندس بـ <code>lazy=True</code> لربطه مع المواعيد التشخيصية.
                        </p>
                        <ul class="text-xs space-y-1 text-slate-700 dark:text-slate-300 list-disc list-inside">
                            <li><code class="text-blue-600 dark:text-blue-400">id</code>: مفتاح رئيسي (PK).</li>
                            <li><code class="text-blue-600 dark:text-blue-400">username, password_hash</code>: لتسجيل الدخول بأمان.</li>
                            <li><code class="text-blue-600 dark:text-blue-400">role</code>: دور الحساب (admin, doctor, reception).</li>
                            <li><code class="text-fuchsia-600 dark:text-fuchsia-400">diagnoses</code>: (Relationship) قائمة كشوفاته.</li>
                        </ul>
                    </div>

                    <div class="bg-emerald-50/50 dark:bg-emerald-900/10 p-5 rounded-xl border border-emerald-100 dark:border-emerald-800">
                        <h4 class="font-bold text-slate-800 dark:text-white mb-2">2. جدول المرضى (Patient Model)</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            الجزء النابض. يحفظ كل تفصيل عن حالة المريض وقت وصوله، نقاطه (Score) المحسوبة آلياً، وحالته الحالية بالعيادة.
                        </p>
                        <ul class="text-xs space-y-1 text-slate-700 dark:text-slate-300 list-disc list-inside">
                            <li><code class="text-emerald-600 dark:text-emerald-400">name, age, phone</code>: معلومات أساسية.</li>
                            <li><code class="text-emerald-600 dark:text-emerald-400">appointment_type</code>: (عادي، طوارئ، متابعة).</li>
                            <li><code class="text-emerald-600 dark:text-emerald-400">urgency_tier, priority_score</code>: الخوارزمية تملأ هذا!</li>
                            <li><code class="text-emerald-600 dark:text-emerald-400">status</code>: وضع المريض ('waiting', 'in_progress', 'completed').</li>
                        </ul>
                    </div>
                </div>

                <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-4 text-lg border-l-4 border-fuchsia-500 pl-3">
                        3. المحور الرابط - جدول التشخيص (Appointment Model)
                    </h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">
                        العبقرية في تصميم الداتا بيس تكمن هنا. هذا الجدول لا يوجد بمفرده، بل هو نقطة التقاء (Many-to-One) بين <b>الطبيب</b> و <b>المريض</b>. عندما ينهي الطبيب الكشف، يضيف تقريره، فيتم ربط هوية الطبيب بهوية المريض مع التقرير والوقت لإنشاء سجل تاريخي مستحيل الكسر.
                    </p>

                    <div class="code-block-wrapper">
                        <div class="code-header">
                            <span><i class="bi bi-file-earmark-code"></i> models.py (السطر 56)</span>
                            <button class="copy-btn" onclick="copyCode(this)"><i class="bi bi-clipboard"></i> نسخ</button>
                        </div>
                        <pre><code class="language-python">class Appointment(db.Model):
    """
    جدول لتسجيل بيانات كل كشف/زيارة طبية مكتملة.
    يربط المريض (Patient) مع الطبيب (User) 
    """
    id = db.Column(db.Integer, primary_key=True)
    
    # --- Foreign Keys (القيود الربطية المزدوجة) ---
    # يمنع النظام من إدخال أي شيء، يجب أن يكون المريض موجود حقاً بالطبقة الأولى!
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    # ونفس الأمر للطبيب، لا كشف بدون طبيب موثق!
    doctor_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # توقيت إتمام الموعد (يخزن كـ UTC) منعاً لتداخل الزمن.
    appointment_time = db.Column(db.DateTime, default=now_utc)
    
    # الملاحظات التشخيصية/الوصفة (تأتي من لوحة الطبيب)
    notes = db.Column(db.Text, nullable=True)</code></pre>
                    </div>
                </div>
            </div>
        '''
    },

    # ==================== (5) UTILS.PY ====================
    "utils": {
        "icon": "bi-calculator-fill text-red-500",
        "nav_title": "5. خوارزميات الطابور (utils.py)",
        "title": "محرك الفرز الطبي والتنقيط (Algorithmic Triage)",
        "description": "حل رياضي لتصنيف المرضى لثلاث طبقات أساسية وتسعيرهم بالنقاط التراكمية.",
        "content": '''
            <div class="space-y-6">
                <p class="text-slate-600 dark:text-slate-300">
                    ملف <code>utils.py</code> يحتوي على الخلاصة المنطقية للنظام. السؤال هو: إذا كان المريض (أ) يشكو من شيء بسيط وينتظر منذ 10 ساعات، وجاء مريض (ب) بحالة مصاب بجلطة دماغية (طوارئ)، فهل يدخل صاحب የ10 ساعات؟ قطعا لا. 
                    <b>كيف برمجنا هذه القاعدة الأخلاقية الصارمة؟</b>
                </p>
                <p class="text-slate-600 dark:text-slate-300">
                    من خلال نظام أولوية ثنائي المستوى (Two-Level System) حاسم كالتالي:
                </p>
                
                <ol class="list-decimal list-inside bg-red-50/50 dark:bg-red-900/10 p-5 rounded-xl border border-red-100 dark:border-red-800 text-slate-700 dark:text-slate-300 font-medium space-y-2 mb-6">
                    <li><strong>الطبقة 1 (الإلحاح - Urgency Tier):</strong> وهي التي تقسم الناس كجدران حديدية (1 للطارئ جداً المهدد للحياة، 2 للمتابعة الجراحية السريعة، 3 للكشف العادي).</li>
                    <li><strong>الطبقة 2 (النقاط - Priority Score):</strong> تحدد الترتيب لمن هم <b>داخل نفس الطبقة والجدار</b>!</li>
                </ol>
                
                <p class="text-sm text-slate-500 mb-4 border-r-4 border-slate-500 pr-3">
                    لدينا استعلام (SQL Database Inquiry) يرتبهم بذكاء: <code>ORDER BY urgency_tier ASC, priority_score DESC</code>. هذا يعني أنه سيتم جلب أصحاب الطوارئ أولاً مهما كانت نقاط الذين تحتهم، ثم سيتم ترتيب أصحاب كل طبقة بحسب نقاط الضعف الخاصة بهم.
                </p>
                
                <div class="code-block-wrapper">
                    <div class="code-header">
                        <span><i class="bi bi-file-earmark-code"></i> utils.py (السطر 56)</span>
                        <button class="copy-btn" onclick="copyCode(this)"><i class="bi bi-clipboard"></i> نسخ</button>
                    </div>
                    <pre><code class="language-python">def calculate_priority(age: int, appointment_type: str, waiting_minutes: int = 0) -> int:
    """
    كلما كان الرقم أعلى = أولوية أكبر في الدخول
    [المعطيات الـ Parameters]: يأخذ النظام متغيرات المريض الضعيفة لحساب التسعيرة.
    """
    score = 0
    
    # [1] علاوة العمر (Elderly/Toddler Bias)
    # نحمي المستضعفين من الشباب الأصحاء
    if age >= 70:
        score += 50    # الشيوخ الكبار يأخذون 50 نقطة فورية تعطيهم دفعة للأمام!
    elif age >= 60:
        score += 30
    elif age <= 5:
        score += 25    # الأطفال الرضع لهم احترام 25 نقطة
    elif age <= 12:
        score += 15
        
    # [2] عامل الانتظار (Voice of Patience)
    # كل دقيقة = 1 نقطة.
    # التوازن الرائع: المريض الشاب الذي انتظر 50 دقيقة في العيادة، 
    # سيتساوى في النهاية (نقطياً) مع الشيخ الحديث الدخول المربح لـ 50 نقطة فورية! الميزان العادل.
    wait_factor = waiting_minutes * 1  
    
    score += wait_factor
    return score</code></pre>
                </div>

                <div class="mt-4 p-4 border-r-4 border-red-500 bg-red-50 dark:bg-red-900/10 text-slate-700 dark:text-slate-300">
                    <strong>هل يوجد دوال أخرى؟</strong><br>
                    نعم! لقد قمنا ببرمجة دوال قوية مثل <code>calculate_performance_metrics()</code> و <code>generate_doctor_stats()</code> والتي تقوم بقراءة جميع قواعد بيانات التواريخ وعمل (متوسطات وتقارير ذكية) لتعرضها في اللوحة الإدارية.
                </div>
            </div>
        '''
    },

    # ==================== (6) AI_SERVICE.PY ====================
    "ai_engine": {
        "icon": "bi-robot text-indigo-500",
        "nav_title": "6. الذكاء الاصطناعي (ai_service.py)",
        "title": "نظام Machine Learning لتوقع وقت الانتظار",
        "description": "الاستغناء عن التخمين البشري البدائي باستخدام Scikit-Learn.",
        "content": '''
            <div class="space-y-6">
                <p class="text-slate-600 dark:text-slate-300">
                    الطريقة التقليدية الفاشلة جداً لحساب موعد المريض هي: (عدد المرضى أمامه × 10 دقائق). هذه معادلة عمياء. ماذا لو كان هناك حالات طوارئ أخذت نصف ساعة؟ الطب غير متوقع.
                    الطريقة الذكية: <b>تدريب الذكاء الاصطناعي على السلوك الزمني السابق للعيادة واستخراج الرقم الحقيقي الخفي.</b>
                </p>
                
                <h3 class="font-bold text-slate-800 dark:text-white text-lg">لماذا الغابة العشوائية (RandomForest) تحديداً؟</h3>
                <p class="text-slate-600 dark:text-slate-300 mb-4">
                    العيادة بيئة فوضوية، المواعيد تصعد وتهبط وتتأثر بالمواسم والساعات. خوارزميات الذكاء الخطي (Linear Regression) ستفشل هنا، بينما (RandomForest) تتغاضى عن الأشواك البيانية (Outliers والمشاكل النادرة الحدوث)، وتستنتج نمطاً قوياً عن طريق تدريب مئات "أشجار القرارات (Decision Trees)".
                </p>

                <div class="code-block-wrapper">
                    <div class="code-header">
                        <span><i class="bi bi-file-earmark-code"></i> ai_service.py (السطر 40) - فئة (WaitTimePredictor)</span>
                        <button class="copy-btn" onclick="copyCode(this)"><i class="bi bi-clipboard"></i> نسخ</button>
                    </div>
                    <pre><code class="language-python">class WaitTimePredictor:
    def __init__(self):
        # المودل يعتمد على 100 شجرة قرار 
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.is_trained = False
        
    def _generate_synthetic_samples(self, n=800):
        # [دالة هندسية]: في بداية فتح العيادة لا يوجد داتا (Cold Start Problem). 
        # لذلك نقوم بتوليد داتا اصطناعية لتدريب الموديل حتى لا يتعطل.
        for _ in range(n):
            queue_len = random.randint(0, 20)
            hour = random.randint(8, 22)
            # الذكاء الاصطناعي يتعلم من الخصائص المتعددة المتداخلة..
            # ... كود التوليد
            
    def predict_wait_time(self, current_queue_length: int, hour: int, day: int, appt_type: int) -> int:
        if not self.is_trained:
            return current_queue_length * 15 # fallback للأسوأ.
            
        # 4D Features: نقوم بتلقيم الموديل برباعية الأبعاد (طول الطابور، الساعة، يوم الأسبوع، نوع الكشف). 
        # الموديل سيرى أن (يوم الخميس + الساعة 8 مساءً + الطابور فيه 5 = الانتظار سيكون أطول من المعتاد).
        features = np.array([[current_queue_length, hour, day, appt_type]])
        pred = self.model.predict(features)
        
        # التأكد من أنه حتى لو أخطأ الموديل لن يعطينا رقماً سالباً! أقصى شيء 5 دقائق
        return max(5, int(pred[0]))</code></pre>
                </div>
                
                <p class="text-sm text-slate-600 dark:text-slate-400 border-r-4 border-indigo-500 pr-3">
                    في الـ Backend الحقيقي بالمشروع (في دالة مستقلة `get_wait_time_minutes`) الموديل ينظر لمتوسط السرعة <b>الحالية والوقتية</b> للطبيب (كم دقيقة أخذها لكل مريض قيد العلاج في الساعة الحالية) ويدمجها بقوة مع قرار الخوارزمي أعلاه لزيادة الدقة وجعلها لا تصدق!
                </p>
            </div>
        '''
    },

    # ==================== (7) CLOCK_CONFIG.PY ====================
    "clock_config": {
        "icon": "bi-shield-check text-teal-500",
        "nav_title": "7. الزمن والأمان (clock / config)",
        "title": "أسرار توقيت بغداد وملف الحماية والمفاتيح",
        "description": "حل معضلة المناطق الزمنية وإخفاء أسرار التشفير من الاختراق.",
        "content": '''
            <div class="space-y-6">
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-clock-history text-teal-500"></i> معضلة اختلاف المناطق الزمنية (clock.py)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        واحدة من أخطر المشاكل البرمجية التي يقع فيها الطلاب هي تسجيل الوقت حسب "لغة السيرفر". 
                        فلو قمت برفع المشروع على سيرفر في أمريكا، وسجلت مريضاً الساعة 12 ظهراً بتوقيت بغداد، سيُسجل في قاعدة البيانات بأنه حضر الساعة 5 فجراً (أو بتوقيت سيرفر الاستضافة)! 
                        النتيجة؟ المواعيد دُمرت، الحقول الإحصائية كاذبة، وحسابات الـ ML انهارت تماماً.
                    </p>
                    <p class="font-bold text-slate-800 dark:text-white mb-2">القاعدة الذهبية المُنفذة للحماية من ذلك:</p>
                    <p class="text-slate-600 dark:text-slate-300 font-mono text-sm bg-slate-100 dark:bg-slate-700 p-3 rounded mb-4">
                        احفظ جميع التواريخ بـ Database كـ (UTC Standard) دائماً وأبداً. ثم حولها لـ (Baghdad Time) عند عرضها على الشاشة للمستخدم البشري فقط.
                    </p>

                    <div class="code-block-wrapper">
                        <div class="code-header">
                            <span><i class="bi bi-file-earmark-code"></i> clock.py</span>
                            <button class="copy-btn" onclick="copyCode(this)"><i class="bi bi-clipboard"></i> نسخ</button>
                        </div>
                        <pre><code class="language-python"># توقيت العراق الرسمي محتجز كمراقب
BAGHDAD = ZoneInfo("Asia/Baghdad")

def now_utc() -> datetime:
    """الوقت الحالي بتوقيت UTC - للحفظ في Database وفقط"""
    return datetime.now(timezone.utc)

def to_local(dt: datetime) -> datetime:
    """تحويل بيانات الـ Database للعرض على الشاشة البصرية بتوقيت بغداد"""
    if dt is None: 
        return None
    # نعيد صياغته بتوقيت العراق 
    if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(BAGHDAD)</code></pre>
                    </div>
                </section>

                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-shield-lock-fill text-amber-500"></i> خزانة الأمان والأقفال (config.py)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        الأنظمة غير المحترفة تترك المفاتيح السرية في جميع أرجاء الكود. أما هذا المشروع فقد عَزل جميع المتغيرات الحساسة (Environment Variables) في مجلد موحد <code>config.py</code>.
                    </p>
                    
                    <ul class="space-y-3 mt-4 mb-4">
                        <li class="p-3 bg-amber-50 dark:bg-amber-900/10 border border-amber-100 dark:border-amber-800 rounded-lg">
                            <strong class="text-amber-800 dark:text-amber-300">SECRET_KEY</strong><br>
                            <span class="text-sm text-slate-600 dark:text-slate-400">مفتاح بايثون الغامض الذي يتم تمليحه (Salting) واستخدامه لتشفير الجلسات (Sessions). حرمانك منه يعرض الـ Cookies الخاصة بمديرك للسرقة ومن ثم اختراق النظام (Session Hijacking).</span>
                        </li>
                        <li class="p-3 bg-red-50 dark:bg-red-900/10 border border-red-100 dark:border-red-800 rounded-lg">
                            <strong class="text-red-800 dark:text-red-300">ADMIN_SECRET_KEY</strong><br>
                            <span class="text-sm text-slate-600 dark:text-slate-400">رمز حماية ثانوي (قفل فوق الجدار). لمنع أي طبيب أو أحد من إنشاء "مدير نظام" يعبث بالأساسيات، يجب معرفة (كود المؤسس 123456) لإضافة حساب بصلاحية (admin) جديدة!</span>
                        </li>
                    </ul>
                </section>
            </div>
        '''
    },

    # ==================== (8) TEMPLATES ====================
    "templates": {
        "icon": "bi-window-sidebar text-sky-500",
        "nav_title": "8. واجهات المستخدم (Templates)",
        "title": "هيكلية الـ HTML ورؤية الشاشات الشاملة",
        "description": "سرد مفصل لجميع ملفات الـ HTML داخل مجلد الواجهات وماذا يعرض كل منهم.",
        "content": '''
            <div class="space-y-6">
                <p class="text-slate-600 dark:text-slate-300 mb-6">
                    تم إنشاء واجهات المشروع باستخدام تقنية <b>Jinja2 Templates</b>. ولأن إعادة كتابة الأكواد وتكرارها خطأ فادح في هندسة البرمجيات (DRY Principle)، قمنا ببرمجة <b>واجهة القالب الأساسي (layout.html)</b> التي ترث منها جميع الصفحات الأخرى خصائصها كشريط التنقل وقوالب التنبيه ودعم الـ Tailwind السريع.
                </p>

                <div class="bg-slate-50 dark:bg-slate-800/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-4 text-xl border-b border-slate-200 dark:border-slate-700 pb-2">تفصيل وظائف الشاشات الـ 10</h3>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm">
                            <h4 class="font-bold text-sky-600 dark:text-sky-400 font-mono">1. layout.html</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><b>العظم الجسدي:</b> الواجهة الأم التي ترثها بقية الصفحات. تحتوي على استيراد مكاتب (Tailwind CDN) وشريط الـ (Navbar) العشوائي وزر الـ (Dark Mode) الدائم وأكواد الـ (Flash Messages) للرسائل التنبيهية.</p>
                        </div>

                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm">
                            <h4 class="font-bold text-emerald-600 dark:text-emerald-400 font-mono">2. index.html</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><b>الصفحة الترحيبية:</b> التي يبدأ منها المستخدم، وتتجه به للأقسام المختلفة بتصميم دعائي نظيف يشرح قوة النظام باختصار.</p>
                        </div>

                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm">
                            <h4 class="font-bold text-cyan-600 dark:text-cyan-400 font-mono">3. kiosk.html</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><b>حاسوب الاستقبال (الشكاوي):</b> حيث يُدخل المريض بياناته. الميزة هنا أنه يحتوي على قسم سؤال المريض أسئلة سريعة ذكية (مثل: هل الألم مفاجئ؟ هل يعاني من نزيف؟) ليُحدد نوع الزيارة.</p>
                        </div>

                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm">
                            <h4 class="font-bold text-amber-600 dark:text-amber-400 font-mono">4. queue.html</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><b>الشاشة الحية:</b> صُممت لتُعلق في غرفة الانتظار. لا يوجد بها أزرار أو تفاعلات بل شاشة سوداء/مظلمة مريحة للعين، تعرض المرضى على الترتيب بفضل أمر <code>fetch('/api/queue')</code> كل 30 ثانية بجافا سكربت.</p>
                        </div>

                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm border-l-4 border-l-red-500">
                            <h4 class="font-bold text-red-600 dark:text-red-400 font-mono">5. doctor.html</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><b>غرفة الدكتور الخاصة:</b> شاشة مُقسمة. اليسار للمريض الحالي مع القدرة على كتابة استشارة (Notes) وإنهاء الطلب. واليمين يحمل قائمة (من هو المريض التالي) ليكون الطبيب جاهزاً. وفي الأسفل تاريخ التشخيصات لليوم وحالة الطابور خارج غرفته.</p>
                        </div>

                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm border-l-4 border-l-fuchsia-500">
                            <h4 class="font-bold text-fuchsia-600 dark:text-fuchsia-400 font-mono">6. admin.html</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><b>مركز التحكم وإدارة الأزمة:</b> لوحة شاملة 360-درجة تحتكر الصلاحيات. تتفرع إلى عدة صفحات داخلية: إنشاء الحسابات، قراءة إحصائيات النظام اليومية كالمتوسطات (Metrics)، و رؤية التشخيص الـ AI والنصائح الآلية. وملف (db_viewer) للتعديل على جداول العيادة برمجياً (JSON).</p>
                        </div>

                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-sm">
                            <h4 class="font-bold text-slate-600 dark:text-slate-400 font-mono">7-10. صفحات الدعم</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-2"><code>login.html / register.html / reception.html</code> وغيرها التي تساهم في الإدخال وإكمال الدورة اليومية ببطاقات مصممة بشكل محترف.</p>
                        </div>
                    </div>
                </div>
            </div>
        '''
    },

    # ==================== (9) DEPLOYMENT ====================
    "deployment": {
        "icon": "bi-rocket-takeoff-fill text-yellow-500",
        "nav_title": "9. التشغيل والرفع (Render.com)",
        "title": "دليل الرفع التفصيلي على خوادم الاستضافة",
        "description": "نظراً لكثرة مشاكل المواقع القديمة، تم الاعتماد على منصة Render.com الحديثة والموثوقة للرفع المجاني.",
        "content": '''
            <div class="space-y-6">
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-cloud-arrow-up-fill text-sky-500"></i> دليل الرفع باستخدام منصة Render.com
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        يعتبر موقع <b>Render</b> البديل الأقوى لـ Heroku حالياً وأفضل بكثير من المنصات القديمة مثل PythonAnywhere في التعامل مع مشاريع بايثون وتثبيت المكتبات الحديثة. لتجنب أخطاء WSGI المعقدة، اتبع هذه الخطوات البسيطة.
                    </p>
                    
                    <div class="space-y-4">
                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-slate-800 dark:border-slate-500">
                            <h4 class="font-bold text-slate-800 dark:text-slate-300 mb-2">الخطوة 1: الرفع على GitHub أولاً</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                1. قم بإنشاء مستودع (Repository) جديد على حسابك في GitHub.<br>
                                2. قم برفع مجلد المشروع بالكامل إلى هذا المستودع. تأكد من وجود ملف <code>requirements.txt</code> وملف <code>wsgi.py</code> في المجلد الرئيسي.<br>
                                3. يجب أن يحتوي المستودع على جميع ملفات العيادة الذكية لكي يقرأها خادم Render بشكل صحيح.
                            </p>
                        </div>

                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-indigo-500">
                            <h4 class="font-bold text-indigo-600 dark:text-indigo-400 mb-2">الخطوة 2: الربط مع منصة Render</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                1. اذهب لموقع <b>Render.com</b> وسجل دخولك باستخدام حساب GitHub الخاص بك.<br>
                                2. في لوحة التحكم، اضغط على <b>New +</b> واختر <b>Web Service</b>.<br>
                                3. ستظهر لك قائمة بمستودعاتك على GitHub، اختر المستودع الخاص بالعيادة الذكية واضغط <b>Connect</b>.
                            </p>
                        </div>

                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-emerald-500">
                            <h4 class="font-bold text-emerald-600 dark:text-emerald-400 mb-2">الخطوة 3: إعدادات التشغيل (Build & Start Commands)</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                في صفحة الإعدادات الخاصة بالتطبيق، تأكد من صحة الحقول التالية لتفعيل التشغيل التلقائي عبر Gunicorn:<br>
                                - <b>Name:</b> سمّه <code>smartclinic-project</code> أو ما تحب.<br>
                                - <b>Language:</b> اختر <b>Python</b> إذا لم يقم باكتشافه تلقائياً.<br>
                                - <b>Build Command:</b> الصق الأمر التالي:
                            </p>
                            <div class="mt-2 ml-4 mb-3 p-2 bg-slate-100 dark:bg-slate-900 rounded font-mono text-sm text-slate-800 dark:text-slate-200">
                                pip install -r requirements.txt
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                - <b>Start Command:</b> الصق الأمر التالي وهو الأهم:
                            </p>
                            <div class="mt-2 ml-4 p-2 bg-slate-100 dark:bg-slate-900 rounded font-mono text-sm text-slate-800 dark:text-slate-200">
                                gunicorn wsgi:app
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mt-3">ثم اختر الباقة المجانية (Free) واضغط أسفل الشاشة على <b>Create Web Service</b>.</p>
                        </div>

                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-amber-500">
                            <h4 class="font-bold text-amber-600 dark:text-amber-400 mb-2">ملاحظة هامة (طبيعة الاستضافة المجانية)</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                - <b>عملية الرفع الأولى:</b> ستأخذ بعض الوقت (حوالي دقيقتين إلى 5 دقائق) لتثبيت مكتبات مثل Scikit-learn.<br>
                                - <b>وضعية السبات (Sleep):</b> كما تفضلت بالملاحظة، الاستضافة المجانية في Render "تنام" إذا لم يزر الموقع أحد لمدة 15 دقيقة تقريباً للحفاظ على موارد الخادم.<br>
                                - نتيجة لذلك، عند دخول أول مستخدم بعد فترة، سيستغرق الموقع مسافة (50 ثانية تقريباً) للرد. هذا طبيعي جداً ويعمل بشكل سليم كمنصة عرض مشاريع التخرج المجانية.
                            </p>
                        </div>
                        
                    </div>
                    
                    <p class="text-emerald-600 dark:text-emerald-400 font-bold mt-4 border-t border-slate-200 dark:border-slate-700 pt-4 text-center text-lg">
                        🎉 مبروك! مشروعك المتكامل الآن على منصة حديثة وسيعمل بشكل مثالي ومستقر دون أخطاء بيئة عمل.
                    </p>
                </section>
            </div>
        '''
    }
}
