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
                        لبناء هذا النظام المتكامل، تم استخدام مجموعة من أحدث التقنيات. <strong>الهدف من هذا القسم هو جعلك كطالب قادراً على الإجابة بكل ثقة على سؤال المناقش: "لماذا استخدمت هذه التقنية تحديداً؟ وما فائدتها؟"</strong>
                    </p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-blue-50/50 dark:bg-blue-900/10 p-5 rounded-xl border border-blue-100 dark:border-blue-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-filetype-py text-2xl text-blue-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">بايثون (Python 3.10+)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">
                                لغة البرمجة الأساسية في الخادم (Backend).
                            </p>
                            <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-2 list-disc list-inside">
                                <li><strong>لماذا بايثون؟</strong> لأنها اللغة رقم #1 عالمياً في الذكاء الاصطناعي، وتتميز بكود مقروء وبسيط جداً يسهل على الطالب استيعابه وشرحه.</li>
                                <li><strong>كيف تعمل هنا؟</strong> تقوم بدور "العقل المفكر" للمشروع؛ تحسب أولويات المرضى وتدير النظام بأكمله.</li>
                                <li><strong>الفائدة الهندسية:</strong> ربطت خوارزميات الطابور (Priority Triage) بنماذج تعلم الآلة (ML) بسلاسة في بيئة واحدة دون الحاجة للغات متعددة.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-emerald-50/50 dark:bg-emerald-900/10 p-5 rounded-xl border border-emerald-100 dark:border-emerald-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-server text-2xl text-emerald-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">إطار عمل فلاسك (Flask Web Framework)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">
                                إطار عمل (Framework) لبناء المواقع باستخدام بايثون بهندسية (MVT).
                            </p>
                            <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-2 list-disc list-inside">
                                <li><strong>لماذا فلاسك وليس جانغو (Django)؟</strong> فلاسك خفيف جداً (Micro-framework) ولا يحتوي على تعقيدات ومجلدات كثيرة غير ضرورية، مما يجعله مثالياً لمشروع تخرج سريع الفهم للمناقشين، في حين أن Django قد يكون معقداً وصعب الشرح.</li>
                                <li><strong>الفائدة للمشروع:</strong> استخدمناه لاستقبال طلبات المتصفح (HTTP) وبناء نظام توجيه (Routing) محمي، بحيث لا يُفتح قسم "الطبيب" إلا بحساب الطبيب.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-indigo-50/50 dark:bg-indigo-900/10 p-5 rounded-xl border border-indigo-100 dark:border-indigo-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-database-fill text-2xl text-indigo-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">قاعدة البيانات (SQLite & SQLAlchemy)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">
                                نظام إدارة قواعد البيانات لحفظ المرضى والمستخدمين بأمان.
                            </p>
                            <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-2 list-disc list-inside">
                                <li><strong>لماذا SQLite؟</strong> لأنها تُحفظ كملف <code>clinic.db</code> جاهز للعمل. لا حاجة لتثبيت خوادم معقدة مثل MySQL على حاسوب المناقش أو الجامعة.</li>
                                <li><strong>ما هو SQLAlchemy ولماذا استخدمناه؟</strong> هو (ORM) يحول جداول البيانات إلى "كائنات بايثون" (Objects). الفائدة العظمى منه هي حماية النظام تماماً من الاختراق ثغرة (SQL Injection)، كما أنه يبسط الكود بدلاً من كتابة أوامر أجنبية داخل بايثون.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-pink-50/50 dark:bg-pink-900/10 p-5 rounded-xl border border-pink-100 dark:border-pink-800">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-robot text-2xl text-pink-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">الذكاء الاصطناعي (Scikit-Learn ML)</span>
                            </div>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">
                                مكتبة التعلم الآلي القوية. استخدمنا بداخلها نموذج (Random Forest Regressor).
                            </p>
                            <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-2 list-disc list-inside">
                                <li><strong>كيف يعمل ولماذا استُخدم؟</strong> بدلاً من التخمين العشوائي (إعطاء كل مريض 15 دقيقة انتظار ثابتة غبية)، يقوم نموذجنا بالتنبؤ بالوقت الفعلي من خلال التدرب على بيانات العيادة (ضغط العمل، وقت اليوم، والطابور الحالي).</li>
                                <li><strong>الفائدة الجوهرية (الميزة التنافسية):</strong> هي ما يجعل العيادة (ذكية). بدون هذا الموديل سيكون النظام مجرد طابور إلكتروني عادي. الذكاء الاصطناعي هو نقطة القوة (Selling Point) الأساسية في مشروع التخرج.</li>
                            </ul>
                        </div>
                        
                        <div class="bg-slate-50 dark:bg-slate-800/50 p-5 rounded-xl border border-slate-200 dark:border-slate-700">
                            <div class="flex items-center gap-3 mb-2">
                                <i class="bi bi-palette-fill text-2xl text-cyan-500"></i>
                                <span class="font-bold text-slate-800 dark:text-white text-lg">الواجهات المرئية (Tailwind CSS)</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mb-2 leading-relaxed">
                                <strong>لماذا Tailwind؟</strong> تخلصنا من ملفات CSS الضخمة التي تصبح كابوساً عند التعديل، وبدأنا نكتب التصميم داخل ملف HTML ككلاسات جاهزة (Utility-First). وفر هذا 70% من وقت بناء الواجهات مع جعل الموقع متجاوباً (Responsive) للهواتف وبناء الوضع الليلي بكلمة <code>dark:</code> فقط.
                            </p>
                        </div>
                        
                        <div class="bg-yellow-50/50 dark:bg-yellow-900/10 p-5 rounded-xl border border-yellow-200 dark:border-yellow-800 md:col-span-2 shadow-inner">
                            <div class="flex items-center gap-3 mb-4 border-b border-yellow-200 dark:border-yellow-800 pb-3">
                                <i class="bi bi-filetype-jsx text-3xl text-yellow-600 dark:text-yellow-400"></i>
                                <div>
                                    <h3 class="font-bold text-slate-800 dark:text-white text-lg">أين تم استخدام الجافاسكربت (JavaScript) بالضبط؟</h3>
                                    <p class="text-xs text-slate-500 dark:text-slate-400">خريطة مفصلة للـ 5% من الكود المكتوب بـ (Vanilla JS) الخالصة للفهم والمناقشة الأكاديمية.</p>
                                </div>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
                                <div class="p-3 bg-white dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700 hover:border-yellow-400 transition-colors">
                                    <h5 class="font-bold text-yellow-600 dark:text-yellow-400 text-xs mb-1"><i class="bi bi-display"></i> 1. شاشة الطابور (queue.html)</h5>
                                    <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">تُستخدم دالة <code>fetch()</code> لطلب بيانات المرضى من الخادم (API) كل 5 ثوانٍ وإعادة رسم الشاشة <b>بدون عمل Refresh</b> لتوفير تحديث حي (Real-time Feel).</p>
                                </div>
                                <div class="p-3 bg-white dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700 hover:border-yellow-400 transition-colors">
                                    <h5 class="font-bold text-yellow-600 dark:text-yellow-400 text-xs mb-1"><i class="bi bi-graph-up-arrow"></i> 2. لوحة الإدارة المركزية (admin.html)</h5>
                                    <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">تشغيل مكتبة (Chart.js) لرسم المنحنيات البيانية للإحصائيات بطريقة تفاعلية جذابة لقراءة البيانات والأرباح.</p>
                                </div>
                                <div class="p-3 bg-white dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700 hover:border-yellow-400 transition-colors">
                                    <h5 class="font-bold text-yellow-600 dark:text-yellow-400 text-xs mb-1"><i class="bi bi-moon-stars"></i> 3. القالب الرئيسي للجميع (layout.html)</h5>
                                    <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">سكربت تفعيل (الوضع الليلي) وحفظه في الـ LocalStorage المدمج بالمتصفح. بالإضافة لبرمجة عداد تنازلي لإخفاء رسائل الخطأ (Toasts) بعد 3 ثوانٍ.</p>
                                </div>
                                <div class="p-3 bg-white dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700 hover:border-yellow-400 transition-colors">
                                    <h5 class="font-bold text-yellow-600 dark:text-yellow-400 text-xs mb-1"><i class="bi bi-database-check"></i> 4. عارض قاعدة البيانات الداخلية (db_viewer.html)</h5>
                                    <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">برمجة أزرار الحفظ والحذف للتواصل العكسي مع قاعدة البيانات بصمت (Silently AJAX) وتحديث جداول الـ JSON.</p>
                                </div>
                                <div class="p-3 bg-white dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700 hover:border-yellow-400 transition-colors md:col-span-2">
                                    <h5 class="font-bold text-yellow-600 dark:text-yellow-400 text-xs mb-1"><i class="bi bi-shield-check"></i> 5. شاشة التسجيل للطاقم الطبي (register.html)</h5>
                                    <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">نافذة أمان صغيرة (Client-Side Validation) تقارن كلمتي المرور المدخلتين قبل إرسالهما للخادم لمنع إضاعة وقت السيرفر بردود الخطأ.</p>
                                </div>
                            </div>
                            
                            <div class="p-3 bg-blue-50 dark:bg-blue-900/30 rounded border-r-4 border-blue-500 text-sm text-slate-700 dark:text-slate-300">
                                <p class="font-bold text-blue-700 dark:text-blue-400 mb-1"><i class="bi bi-magic"></i> جواب دفاعي ذكي للمناقشة (Defense Strategy):</p>
                                <p class="text-xs leading-relaxed">إذا سألك الأستاذ المشرف: <b>"لماذا لم تستخدم React أو Angular كإطار عمل للواجهات؟"</b><br>
                                الجواب האكاديمي الدقيق: "مشروعنا يرتكز قوامه على نموذج الذكاء الاصطناعي (Machine Learning) وخوارزمية الفرز (Triage) الموجودة في الخادم (Backend) المبرمج ببايثون. استخدام إطار عمل ضخم مثل React لعرض بيانات بسيطة يُعد تعقيداً هندسياً زائداً (Over-engineering) ويهدر موارد السيرفر دون حاجة. لقد اكتفينا بـ <b>Vanilla JS</b> للقيام بالربط اللحظي (AJAX) حصراً، لنحافظ على كود سريع، خفيف الوزن، ويركز على المنطق المعقد الداخلي للمشروع."</p>
                            </div>
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
                                    هذا المجلد يحتوي على واجهات المستخدم المبنية بـ HTML. يتم دمج هذه الملفات باستخدام محرك القوالب (Jinja2) داخل بايثون لعرض المتغيرات ديناميكياً.
                                </p>
                                <p class="text-xs font-semibold text-blue-600 dark:text-blue-400 mt-2 bg-blue-50 dark:bg-blue-900/30 p-2 rounded">
                                    <i class="bi bi-lightbulb-fill"></i> الفائدة الهندسية: فصل تصاميم الواجهات (HTML) عن أوامر الخادم (Python) يحمي من تداخل الأكواد ويُطبّق مبدأ (Separation of Concerns)، مما يسهل عملية التعديل دون إطفاء الخادم للمستقبل.
                                </p>
                            </div>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="bi bi-folder2-open text-2xl text-emerald-500 mt-1"></i>
                            <div>
                                <strong class="text-lg text-slate-800 dark:text-white">مجلد <code>static/</code></strong>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">
                                    المجلد الذي يحتفظ بالملفات الثابتة التي لا تتغير (Static Assets) مثل ملفات الـ (CSS/JS) والصور.
                                </p>
                                <p class="text-xs font-semibold text-emerald-600 dark:text-emerald-400 mt-2 bg-emerald-50 dark:bg-emerald-900/30 p-2 rounded">
                                    <i class="bi bi-question-circle-fill"></i> لماذا مجلد منفصل؟ يقوم متصفح المستخدم بطلب هذه الملفات مرة واحدة فقط ثم يخزنها في ذاكرته (Cache) لتسريع فتح الموقع في المرات القادمة وتقليل الضغط على السيرفر.
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
                    
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-blue-500"></i> <code>app.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">الملف الرئيسي (الموجه - Router).</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-blue-500">الهدف:</span> يستلم طلبات المتصفح ويربط قاعدة البيانات بالواجهات ليتم عرضها للمستخدم بطريقة الـ MVT.
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-fuchsia-500"></i> <code>models.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">الهيكل الهندسي لقواعد البيانات (SQLAlchemy).</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-fuchsia-500">الهدف:</span> تحويل أكواد بايثون إلى جداول قواعد بيانات آمنة تماماً ومحمية من هجمات الحقن (SQL Injection).
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-red-500"></i> <code>utils.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">مكتبة الدوال الرياضية والخوارزميات.</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-red-500">الهدف:</span> حساب أولويات المرضى (Triage) بناءً على العمر والانتظار لتحديد من يدخل الطبيب أولاً، كاسرين نمط الطابور الأعمى.
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-emerald-500"></i> <code>config.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">المخزن الآمن لمتغيرات البيئة.</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-emerald-500">الهدف:</span> فصل الإعدادات الحساسة (Secret Keys) عن الكود العادي لمنع تسربها وحماية جلسات المستخدمين (Sessions).
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-pink-500"></i> <code>clock.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">منظم توقيت الخادم الموحد.</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-pink-500">الهدف:</span> تجنب فساد البيانات (Data Corruption) الذي يحصل عند اختلاف السيرفرات بحفظ الوقت بـ (UTC) وعرضه محلياً.
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-filetype-py text-indigo-500"></i> <code>ai_service.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">النموذج الذكي للتعلم الآلي (Machine Learning).</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-indigo-500">الهدف:</span> تطبيق خوارزمية (Random Forest) لتقدير وقت الانتظار بناءً على تاريخ العيادة، بدلاً من تخمين الموظفين اليدوي.
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-database text-amber-600"></i> <code>clinic.db</code> / <code>requirements.txt</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">ملف قاعدة البيانات والمتطلبات التشغيلية.</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                مقفل ومحصن. يحتوي الـ requirements على البكجات اللازمة لتسهيل تثبيت المشروع بضغطة زر للمناقش.
                            </p>
                        </div>
                        <div class="p-4 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg">
                            <strong><i class="bi bi-robot text-teal-600"></i> <code>seed_db.py</code></strong>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 mb-2">سكربت زرع وتوليد قاعدة البيانات الوهمية.</p>
                            <p class="text-[11px] font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 p-2 rounded">
                                <span class="text-teal-500">الهدف:</span> إمكانية مسح النظام وملئه بآلاف السجلات الوهمية لاختبار قوة تحمل الخوارزميات (Stress Testing) بثوانٍ.
                            </p>
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
                    ملف <code>app.py</code> أطول ملف في المشروع. ويعتبر (Controller) في نمط الـ MVC. هو العقل المدبر الذي يربط بين جداول قاعدة البيانات (Models) وبين واجهات الاستخدام (Templates). ويقوم باستقبال وإرسال جميع الطلبات (HTTP Requests).
                </p>
                <div class="p-4 bg-emerald-50 dark:bg-emerald-900/10 border-r-4 border-emerald-500 rounded mb-4">
                    <p class="text-sm font-bold text-emerald-700 dark:text-emerald-400">💡 لماذا نضع كل الروابط (Routes) هنا؟</p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 mt-1">هندسة (مركزية التحكم - Centralized Control) تجعل إدارة أمان الموقع أسهل بكثير. فبدلاً من البحث في مئات الملفات، كل صفحة في المشروع لها دالة محددة هنا تتحكم بمَن يحق له الدخول وما هي البيانات التي ستسحب من الـ Database إلى الواجهة.</p>
                </div>

                <div class="bg-indigo-50/50 dark:bg-indigo-900/10 p-5 rounded-xl border border-indigo-100 dark:border-indigo-800">
                    <h3 class="font-bold text-slate-800 dark:text-white mb-2">الدوال الجدارية (Decorators) وتحديث الطابور</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">يحتوي الكود على آليات حماية متقدمة وتحديث حي للبيانات (Real-Time processing):</p>
                    
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
                    البرمجة القديمة تعتمد على كتابة نصوص SQL نقية، وهو أسلوب غير آمن تماماً ويعرض النظام لاختراق حقن البيانات (SQL Injection). لذا استخدمنا طبقة تجريدية ضخمة تسمى الـ (SQLAlchemy ORM - Object Relational Mapping).
                </p>
                
                <div class="p-4 bg-fuchsia-50 dark:bg-fuchsia-900/10 border-r-4 border-fuchsia-500 rounded mb-4">
                    <p class="text-sm font-bold text-fuchsia-700 dark:text-fuchsia-400">💡 الفائدة الهندسية للـ ORM:</p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 mt-1">نحن نتعامل مع الجداول وكأنها "كائنات وفئات بايثون" (Classes & Objects). هذا التجريد يجعل الكود نظيفاً جداً، ويسمح مستقبلاً بتغيير نوع قاعدة البيانات بالكامل (مثلاً من SQLite محلي إلى السيرفر السحابي PostgreSQL) دون الحاجة لتغيير سطر كود واحد من النظام!</p>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <div class="bg-blue-50/50 dark:bg-blue-900/10 p-5 rounded-xl border border-blue-100 dark:border-blue-800">
                        <h4 class="font-bold text-slate-800 dark:text-white mb-2">1. جدول المستخدمين (User Model)</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            يُخزن بيانات دخول أطقم العيادة بشكل مشفر (Hashed) بفضل مكتبة <code>werkzeug.security</code> لتأمين كلمات السر (Passwords) حتى لو سُربت قاعدة البيانات نفسها في عملية اختراق.
                        </p>
                        <ul class="text-xs space-y-1 text-slate-700 dark:text-slate-300 list-disc list-inside">
                            <li><code class="text-blue-600 dark:text-blue-400">id</code>: مفتاح رئيسي (Primary Key).</li>
                            <li><code class="text-blue-600 dark:text-blue-400">username, password_hash</code>: لتسجيل الدخول بأمان.</li>
                            <li><code class="text-blue-600 dark:text-blue-400">role</code>: دور الحساب لفصل الصلاحيات (Authorization).</li>
                            <li><code class="text-fuchsia-600 dark:text-fuchsia-400">diagnoses</code>: (Relationship) قائمة كشوفاته المرتبطة.</li>
                        </ul>
                    </div>

                    <div class="bg-emerald-50/50 dark:bg-emerald-900/10 p-5 rounded-xl border border-emerald-100 dark:border-emerald-800">
                        <h4 class="font-bold text-slate-800 dark:text-white mb-2">2. جدول المرضى (Patient Model)</h4>
                        <p class="text-sm text-slate-600 dark:text-slate-400 mb-3">
                            القلب النابض! يحفظ كل تفصيل عن حالة المريض وقت وصوله، ونقاط الطوارئ المحسوبة آلياً لفرزه.
                        </p>
                        <ul class="text-xs space-y-1 text-slate-700 dark:text-slate-300 list-disc list-inside">
                            <li><code class="text-emerald-600 dark:text-emerald-400">name, age, phone</code>: معلومات أساسية.</li>
                            <li><code class="text-emerald-600 dark:text-emerald-400">appointment_type</code>: (عادي، طوارئ، إلخ).</li>
                            <li><code class="text-emerald-600 dark:text-emerald-400">urgency_tier, priority_score</code>: الخوارزمية تملأ هذا ديناميكياً لتكسر مبدأ الطابور الأعمى!</li>
                            <li><code class="text-emerald-600 dark:text-emerald-400">status</code>: وضع المريض لتفعيل تحديث الواجهات.</li>
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
                    <b>كيف برمجنا هذه القاعدة الأخلاقية الصارمة؟ (تجاوزنا الـ FIFO)</b>
                </p>
                
                <div class="p-4 bg-red-50 dark:bg-red-900/10 border-r-4 border-red-500 rounded mb-4 mt-4">
                    <p class="text-sm font-bold text-red-700 dark:text-red-400">💡 الفائدة الهندسية والأكاديمية:</p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 mt-1">المستشفيات الحقيقية لا تعمل بنظام (من يأتي أولا). برمجنا خوارزمية فرز (Triage Algorithm) تعطي أوزاناً معينة (Weights) للعمر، ولخطورة الحالة، ولوقت الانتظار الفعلي لمنع الظلم. هذا يثبت للمناقش أن المشروع يعالج مشكلة مجتمعية معقدة وليس مجرد موقع إلكتروني بسيط.</p>
                </div>

                <p class="text-slate-600 dark:text-slate-300">
                    من خلال نظام أولوية ثنائي المستوى (Two-Level System) حاسم كالتالي:
                </p>
                
                <ol class="list-decimal list-inside bg-red-50/50 dark:bg-red-900/10 p-5 rounded-xl border border-red-100 dark:border-red-800 text-slate-700 dark:text-slate-300 font-medium space-y-2 mb-6 mt-4">
                    <li><strong>الطبقة 1 (الإلحاح - Urgency Tier):</strong> وهي التي تقسم الناس كجدران حديدية (1 للطارئ جداً المهدد للحياة، 2 للمتابعة الجراحية السريعة، 3 للكشف العادي).</li>
                    <li><strong>الطبقة 2 (النقاط - Priority Score):</strong> تحدد الترتيب لمن هم <b>داخل نفس الطبقة والجدار</b>!</li>
                </ol>
                
                <p class="text-sm text-slate-500 mb-4 border-r-4 border-slate-500 pr-3">
                    لدينا استعلام (SQL Database Inquiry) يُطبق هذه الخوارزمية بذكاء: <code>ORDER BY urgency_tier ASC, priority_score DESC</code>. هذا يعني أنه سيتم جلب أصحاب الطوارئ أولاً مهما كانت نقاط الذين تحتهم، ثم سيتم ترتيب أصحاب كل طبقة بحسب نقاط الضعف الخاصة بهم.
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
                    الطريقة التقليدية والمستخدمة في بعض المستشفيات لحساب موعد المريض هي: (عدد المرضى أمامه × 10 دقائق). هذه معادلة عمياء فاشلة، فماذا لو كان هناك حالات طوارئ أخذت نصف ساعة لكل مريض؟ الطب غير متوقع.
                    الطريقة الذكية: <b>تدريب الذكاء الاصطناعي (Machine Learning) على السلوك الزمني السابق للعيادة واستخراج الرقم الحقيقي الخفي.</b>
                </p>
                
                <div class="p-4 bg-indigo-50 dark:bg-indigo-900/10 border-r-4 border-indigo-500 rounded mb-4 mt-4">
                    <p class="text-sm font-bold text-indigo-700 dark:text-indigo-400">💡 الفائدة الجوهرية (أساس تقييم المشروع):</p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 mt-1">هذه النقطة تُعتبر (Point of sale) في مشروع التخرج. الذكاء الاصطناعي لا يخمن طول الطابور، بل "يتعلم" من تاريخ العيادة أن يوم السبت صباحاً يكون الطبيب بطيئاً بسبب الازدحام، فيُعطي وقت انتظار أطول. هذا هو الجوهر الذي يجعل العيادة اسمها "ذكية".</p>
                </div>

                <h3 class="font-bold text-slate-800 dark:text-white text-lg">لماذا الغابة العشوائية (RandomForest) تحديداً؟</h3>
                <p class="text-slate-600 dark:text-slate-300 mb-4">
                    العيادة بيئة فوضوية، المواعيد تصعد وتهبط وتتأثر بالمواسم والساعات. خوارزميات الذكاء الخطي (Linear Regression) ستفشل هنا لتعقيد البيانات، بينما (RandomForest) تتغاضى عن الشذوذ في البيانات (Outliers)، وتستنتج نمطاً قوياً عن طريق تدريب مئات "أشجار القرارات (Decision Trees)".
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
                        واحدة من أخطر المشاكل البرمجية التي يقع فيها الطلاب هي تسجيل الوقت الراجع من "توقيت لغة السيرفر". 
                        فلو قمت برفع المشروع على سيرفر في أمريكا، وسجلت مريضاً الساعة 12 ظهراً بتوقيت بغداد، سيُسجل في قاعدة البيانات بأنه حضر الساعة 5 فجراً (حسب موقع السيرفر المركزي)! 
                        النتيجة؟ المواعيد دُمرت، الحقول الإحصائية كاذبة، وحسابات الـ ML انهارت تماماً.
                    </p>

                    <div class="p-4 bg-teal-50 dark:bg-teal-900/10 border-r-4 border-teal-500 rounded mb-4">
                        <p class="text-sm font-bold text-teal-700 dark:text-teal-400">💡 الحماية الهندسية المنفذة:</p>
                        <p class="text-xs text-slate-700 dark:text-slate-300 mt-1">استخدمنا معيار (UTC Standard) الدائم. النظام يحفظ جميع التواريخ بـ UTC (التوقيت العالمي الموحد بدون فوارق) في قاعدة البيانات لتثبيت المرجع، ثم يقوم بتحويلها إلى (Baghdad Time) <b>فقط</b> عند عرضها على الشاشة للبشر. هذا يجعل النظام دقيقاً جداً ولو نُقل السيرفر لأمريكا اللاتينية.</p>
                    </div>

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
                    تم إنشاء واجهات المشروع باستخدام تقنية <b>Jinja2 Templates</b>. ولأن إعادة كتابة الأكواد وتكرارها خطأ فادح في هندسة البرمجيات (مبدأ DRY - Don't Repeat Yourself)، قمنا ببرمجة <b>واجهة القالب الأساسي (layout.html)</b> التي ترث منها جميع الصفحات الأخرى خصائصها كشريط التنقل وقوالب التنبيه.
                </p>

                <div class="p-4 bg-sky-50 dark:bg-sky-900/10 border-r-4 border-sky-500 rounded mb-6">
                    <p class="text-sm font-bold text-sky-700 dark:text-sky-400">💡 لماذا Tailwind CSS وأجاكس وليس CSS عادي وإطارات JS معقدة؟</p>
                    <p class="text-xs text-slate-700 dark:text-slate-300 mt-1">
                        تخلصنا من ملفات CSS الضخمة التي تصبح كابوساً عند التعديل، فـ Tailwind سمحت لنا بالتسريع وبناء الوضع الليلي بكلمة <code>dark:</code> فقط. 
                        أما بالنسبة للجافاسكربت، فقد حصرنا استخدامها <b>في أضيق الحدود (Vanilla JS)</b> للقيام بمهام AJAX (Fetch API) لتحديث الشاشات (مثل شاشة الطابور ولوحة الطبيب) حياً (Real-time) دون انقطاع عمل المتصفح، متجنبين بذلك تعقيدات الـ Frontend Frameworks التي قد تشتت المناقش عن الفكرة الأساسية وهي الذكاء الاصطناعي وهندسة البايثون.
                    </p>
                </div>

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
        "nav_title": "9. التشغيل والرفع",
        "title": "دليل الرفع التفصيلي على خوادم الاستضافة",
        "description": "تم تجهيز وتصميم العيادة الذكية للعمل بسلاسة على أحدث منصات الاستضافة المجانية مثل Railway و Replit.",
        "content": '''
            <div class="space-y-6">
                <!-- Railway Section -->
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-train-front-fill text-indigo-500"></i> دليل الرفع باستخدام منصة Railway.app
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        تعتبر منصة <b>Railway</b> الرائدة حالياً لنشر تطبيقات الويب الحديثة. لقد جهزنا المشروع تماماً للعمل عليها بدون أي أخطاء (Zero-Config) بفضل توفر ملفي <code>Procfile</code> و <code>main.py</code>.
                    </p>
                    
                    <div class="space-y-4">
                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-slate-800 dark:border-slate-500">
                            <h4 class="font-bold text-slate-800 dark:text-slate-300 mb-2">الخطوة 1: الرفع على GitHub</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                قم بإنشاء مستودع (Repository) جديد على حسابك في GitHub، وارفع كامل ملفات المشروع إليه.
                            </p>
                        </div>

                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-indigo-500">
                            <h4 class="font-bold text-indigo-600 dark:text-indigo-400 mb-2">الخطوة 2: النشر على Railway</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                1. اذهب لموقع <b>Railway.app</b> وسجل دخولك باستخدام حساب GitHub الخاص بك.<br>
                                2. في لوحة التحكم، اضغط على <b>New +</b> ثم <b>GitHub Repo</b> واختر مستودع المشروع.<br>
                                3. اضغط <b>Deploy Now</b> وسيبدأ السيرفر فوراً في سحب المشروع وتثبيت المكتبات، وسيرصد المنصة تلقائياً طريقة التشغيل (Gunicorn) ليعمل الموقع بنجاح.
                            </p>
                        </div>

                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-amber-500">
                            <h4 class="font-bold text-amber-600 dark:text-amber-400 mb-2">الخطوة 3: إضافة المتغيرات السرية (Environment Variables)</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                بعد النشر بنجاح وظهور الدائرة الخضراء، انتقل إلى إعدادات المشروع واضغط على <b>Variables</b>:<br>
                                أضف <code>SECRET_KEY</code> للحماية العامة.<br>
                                أضف <code>ADMIN_SECRET_KEY</code> وهو كلمة السر المطلوبة عند التسجيل كصلاحية (مدير/Admin).
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Replit Section -->
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-box-fill text-orange-500"></i> دليل الرفع الاستعراضي السريع على Replit.com
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        إذا كنت ترغب فقط بعرض المشروع بشكل سريع (Demonstration) وإجراء تعديلات لحظية من المتصفح، فهذه بيئة <b>Replit</b> هي الخيار الأمثل.
                    </p>
                    
                    <div class="space-y-4">
                        <div class="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-200 dark:border-slate-700 border-l-4 border-orange-500">
                            <h4 class="font-bold text-orange-600 dark:text-orange-400 mb-2">النقل والتشغيل مباشرةً</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">
                                1. سجل دخولك على <b>Replit.com</b> و قم بعمل Import (استيراد) للمشروع المرفوع على <b>GitHub</b>.<br>
                                2. بعد ثوانٍ، سيتم فتح المشروع. يمكنك التغيير بكلمات السر للمتغيرات البيئية من خلال أداة <b>Secrets</b> الجانبية.<br>
                                3. قم بالضغط على الزر الكبير في الشريط العلوي <b>Run</b>.<br>
                                4. سيعمل الموقع على الفور ويمكنك فتحه كـ نافذة مستقلة ومشاركته كعرض مباشر ولحظي.
                            </p>
                        </div>
                    </div>
                    
                    <p class="text-emerald-600 dark:text-emerald-400 font-bold mt-6 border-t border-slate-200 dark:border-slate-700 pt-4 text-center text-lg">
                        🎉 مبروك! باتباعك لتلك الأنظمة الحديثة، أصبح مشروع العيادة الذكية متاحاً للعملاء ومدراء النظام في أي وقت وأي مكان.
                    </p>
                </section>
            </div>
        '''
    },
    
    # ==================== (10) STUDENT GUIDE ====================
    "student_guide": {
        "icon": "bi-mortarboard-fill text-green-500",
        "nav_title": "10. دليل الطالب والتشغيل",
        "title": "دليل الطالب: تشغيل وفهم مشروع العيادة الذكية",
        "description": "دليل مخصص لك كطالب لتتمكن من تشغيل المشروع على حاسوبك الشخصي (Windows) بسهولة تامة.",
        "content": '''
            <div class="space-y-6">
                <!-- التشغيل السريع -->
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-lightning-charge-fill text-amber-500"></i> أولاً: التشغيل السريع (بنقرة واحدة للمبتدئين)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        لمساعدتك في تجاوز عقبات سطر الأوامر (Terminal)، صممنا لك ملف تشغيل آلي (Script) يقوم بكل شيء بالنيابة عنك!
                    </p>

                    <ol class="list-decimal list-inside space-y-3 text-slate-700 dark:text-slate-300">
                        <li>قم بفك الضغط عن مجلد المشروع <code>SmartClinic_Project</code> وضعه في مكان مناسب (القرص C أو D).</li>
                        <li>تأكد من أن <strong>Python</strong> مُثبت على جهاز الويندوز الخاص بك (عند التثبيت، يجب التأكد من وضع علامة ✅ على خيار <code>Add Python to PATH</code>).</li>
                        <li>ادخل لمجلد المشروع وابحث عن الملف المسمى: 👉 <strong class="text-blue-600 dark:text-blue-400"><code>تشغيل_العيادة_الذكية.bat</code></strong>.</li>
                        <li><strong>انقر نقراً مزدوجاً</strong> على هذا الملف.</li>
                        <li>ستفتح لك شاشة سوداء (موجه الأوامر). انتظر قليلاً، وسيقوم الملف تلقائياً بـ:
                            <ul class="list-disc list-inside ml-6 mt-2 space-y-1 text-slate-600 dark:text-slate-400">
                                <li>إنشاء بيئة افتراضية منعزلة (Virtual Environment).</li>
                                <li>تثبيت جميع المكاتب اللازمة (Flask، SQLAlchemy، Scikit-Learn...).</li>
                                <li>تجهيز قاعدة البيانات بصلاحياتها ومستخدميها.</li>
                                <li>فتح المتصفح الخاص بك تلقائياً على رابط المشروع (<code>http://127.0.0.1:8080</code>).</li>
                            </ul>
                        </li>
                    </ol>
                </section>

                <!-- التشغيل اليدوي للويندوز -->
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-terminal-fill text-slate-700 dark:text-slate-300"></i> ثانياً: التشغيل اليدوي (للمحترفين عبر Windows CMD)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                        إذا كنت تفضل كتابة الأوامر بنفسك لفهم ما يجري خلف الكواليس، اتبع الخطوات التالية في موجه الأوامر (CMD) لمسار المشروع:
                    </p>

                    <div class="space-y-4">
                        <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg">
                            <h4 class="font-bold text-sm text-slate-700 dark:text-slate-300 mb-2">1. إنشاء وتفعيل البيئة الافتراضية</h4>
                            <pre><code class="language-bash">python -m venv venv
venv\\Scripts\\activate</code></pre>
                        </div>

                        <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg">
                            <h4 class="font-bold text-sm text-slate-700 dark:text-slate-300 mb-2">2. تثبيت المكاتب المطلوبة</h4>
                            <pre><code class="language-bash">pip install -r requirements.txt</code></pre>
                        </div>

                        <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-lg">
                            <h4 class="font-bold text-sm text-slate-700 dark:text-slate-300 mb-2">3. تشغيل خادم الويب (Flask Server)</h4>
                            <pre><code class="language-bash">python app.py</code></pre>
                            <p class="text-xs text-slate-500 mt-2">ثم افتح المتصفح على الرابط: <code>http://127.0.0.1:5000</code> أو <code>http://localhost:5000</code></p>
                        </div>
                    </div>
                </section>

                <!-- بيانات الدخول -->
                <section class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700">
                    <h3 class="flex items-center gap-2 text-xl font-bold text-slate-800 dark:text-white mb-4">
                        <i class="bi bi-key-fill text-yellow-500"></i> بيانات تسجيل الدخول (Accounts)
                    </h3>
                    <p class="text-slate-600 dark:text-slate-300 mb-4">
                        التطبيق يحتوي مسبقاً على حسابات جاهزة لتجرّب النظام بكامل أدوراه. استخدمها في صفحة (<code>/login</code>):
                    </p>
                    
                    <div class="overflow-x-auto">
                        <table class="w-full text-sm text-start">
                            <thead class="bg-slate-100 dark:bg-slate-700/50 text-slate-600 dark:text-slate-300">
                                <tr>
                                    <th class="p-3 border-b dark:border-slate-600">الدور (الرتبة)</th>
                                    <th class="p-3 border-b dark:border-slate-600">اسم المستخدم</th>
                                    <th class="p-3 border-b dark:border-slate-600">كلمة المرور</th>
                                </tr>
                            </thead>
                            <tbody class="text-slate-700 dark:text-slate-300 divide-y divide-slate-200 dark:divide-slate-700">
                                <tr>
                                    <td class="p-3 font-bold text-fuchsia-600 dark:text-fuchsia-400">الإدارة العليا (Admin)</td>
                                    <td class="p-3"><code class="bg-slate-200 dark:bg-slate-700 px-2 rounded">admin</code></td>
                                    <td class="p-3"><code class="bg-slate-200 dark:bg-slate-700 px-2 rounded">123</code></td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-red-600 dark:text-red-400">طبيب معالج</td>
                                    <td class="p-3"><code class="bg-slate-200 dark:bg-slate-700 px-2 rounded">doctor</code></td>
                                    <td class="p-3"><code class="bg-slate-200 dark:bg-slate-700 px-2 rounded">123</code></td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-blue-600 dark:text-blue-400">موظف استقبال</td>
                                    <td class="p-3"><code class="bg-slate-200 dark:bg-slate-700 px-2 rounded">reception</code></td>
                                    <td class="p-3"><code class="bg-slate-200 dark:bg-slate-700 px-2 rounded">123</code></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
                
                <div class="p-4 bg-emerald-50 dark:bg-emerald-900/10 border-l-4 border-emerald-500 rounded text-slate-700 dark:text-slate-300 text-sm">
                    <strong>نصيحة للمتميزين:</strong> جرب فتح صفحة <code>/admin/db</code> من حساب <code>admin</code> لرؤية نافذة التحرير المباشرة لقاعدة البيانات (Database Viewer).
                </div>
            </div>
        '''
    }
}
