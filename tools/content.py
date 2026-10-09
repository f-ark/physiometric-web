"""Sitenin bütün metinleri. Dil kuralları uygulamayla aynıdır (K-02, K-27):
fitness uygulamasıdır; ağrı, tanı, tedavi, fizyoterapist, hasta, bozukluk, risk, "düzeltir" ve
karşılıkları kullanılmaz; sonuç, oran ve süre sözü verilmez. Ana sayfa "sen/du/tú", hukuki sayfalar resmi.
"""

LANGS = ("tr", "en", "de", "es")

UI = {
    "tr": {
        "locale": "tr_TR", "theme": "Açık ya da koyu tema", "lang_name": "Türkçe", "play_hl": "tr", "play_small": "Hemen indir", "soon": "Yakında",
        "skip": "İçeriğe geç", "home": "Ana sayfa", "nav_label": "Sayfa menüsü", "lang_label": "Dil",
        "footer_label": "Bağlantılar", "contact": "İletişim", "updated": "Son güncelleme",
        "nav": [("try", "Dene"), ("coach", "Koçun"), ("how", "Nasıl çalışır"), ("pricing", "Ücretsiz ve Pro"), ("faq", "SSS")],
        "links": {"privacy": "Gizlilik Politikası", "terms": "Kullanım Şartları", "developer": "Hakkımızda", "delete-account": "Hesap Silme"},
        "tagline": "Duruşunu ölç, sana göre kurulan kısa bir planla her gün hareket et.",
        "disclaimer": "PosMetric bir fitness uygulamasıdır; tıbbi cihaz değildir.",
        "days": ["Pt", "Sa", "Ça", "Pe", "Cu", "Ct", "Pz"],
        "nf": "Aradığın sayfa bulunamadı.",
    },
    "en": {
        "locale": "en_US", "theme": "Light or dark theme", "lang_name": "English", "play_hl": "en", "play_small": "Get it on", "soon": "Coming soon",
        "skip": "Skip to content", "home": "Home", "nav_label": "Page menu", "lang_label": "Language",
        "footer_label": "Links", "contact": "Contact", "updated": "Last updated",
        "nav": [("try", "Try it"), ("coach", "Your coach"), ("how", "How it works"), ("pricing", "Free and Pro"), ("faq", "FAQ")],
        "links": {"privacy": "Privacy Policy", "terms": "Terms of Use", "developer": "About us", "delete-account": "Delete Account"},
        "tagline": "Measure your posture and move every day with a short plan built around you.",
        "disclaimer": "PosMetric is a fitness app, not a medical device.",
        "days": ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"],
        "nf": "We couldn't find that page.",
    },
    "de": {
        "locale": "de_DE", "theme": "Helles oder dunkles Design", "lang_name": "Deutsch", "play_hl": "de", "play_small": "Jetzt bei", "soon": "Demnächst",
        "skip": "Zum Inhalt", "home": "Startseite", "nav_label": "Seitenmenü", "lang_label": "Sprache",
        "footer_label": "Links", "contact": "Kontakt", "updated": "Zuletzt aktualisiert",
        "nav": [("try", "Ausprobieren"), ("coach", "Dein Coach"), ("how", "So funktioniert's"), ("pricing", "Kostenlos und Pro"), ("faq", "FAQ")],
        "links": {"privacy": "Datenschutz", "terms": "Nutzungsbedingungen", "developer": "Über uns", "delete-account": "Konto löschen"},
        "tagline": "Miss deine Haltung und beweg dich jeden Tag mit einem kurzen Plan, der zu dir passt.",
        "disclaimer": "PosMetric ist eine Fitness-App und kein Medizinprodukt.",
        "days": ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"],
        "nf": "Diese Seite gibt es leider nicht.",
    },
    "es": {
        "locale": "es_ES", "theme": "Tema claro u oscuro", "lang_name": "Español", "play_hl": "es", "play_small": "Disponible en", "soon": "Próximamente",
        "skip": "Ir al contenido", "home": "Inicio", "nav_label": "Menú de la página", "lang_label": "Idioma",
        "footer_label": "Enlaces", "contact": "Contacto", "updated": "Última actualización",
        "nav": [("try", "Pruébalo"), ("coach", "Tu coach"), ("how", "Cómo funciona"), ("pricing", "Gratis y Pro"), ("faq", "Preguntas")],
        "links": {"privacy": "Política de privacidad", "terms": "Términos de uso", "developer": "Sobre nosotros", "delete-account": "Eliminar cuenta"},
        "tagline": "Mide tu postura y muévete cada día con un plan corto hecho para ti.",
        "disclaimer": "PosMetric es una app de fitness, no un dispositivo médico.",
        "days": ["Lu", "Ma", "Mi", "Ju", "Vi", "Sá", "Do"],
        "nf": "No encontramos esa página.",
    },
}

# Paket kimlikleri uygulamadaki görsellerle aynı: assets/images/paket/paket_{kimlik}_{koç}.webp
PACK_IDS = ["masaBasi", "boyunOmuz", "dikDurus", "bel", "sabah", "aksam"]
MOVE_IDS = ["shoulder_elevation", "glute_bridge", "cat_cow"]

HOME = {
    "tr": {
        "title": "PosMetric — Duruş antrenmanı ve kişisel koç",
        "desc": "Telefon kameranla duruşunu ölç, sana göre kurulan kısa bir planla her gün hareket et. Koçun Elif ya da Asım her harekette yanında. Ücretsiz başla.",
        "eyebrow": "Duruş antrenmanı · Kişisel koç",
        "h1": "Ölç. Hareket et. <span>İlerle.</span>",
        "lead": "PosMetric telefon kameranla duruşunu ölçer, sana göre kısa bir antrenman planı kurar ve gelişimini dürüstçe gösterir. Koçun her harekette yanında.",
        "try_btn": "Tarayıcında dene",
        "try_hint": "Kurulum yok · 30 saniye · Görüntü cihazında kalır",
        "try_title": "Duruşuna şimdi bak",
        "try_sub": "Uygulamadaki ölçümün aynısı, tarayıcında. Koçun seni sesle yerine yönlendirir; doğru durduğunda ölçüm kendiliğinden yapılır.",
        "demo_caption": "Örnek fotoğrafta gerçek ölçüm",
        "fine": "Ücretsiz başla · Hesap açman gerekmez · Reklam yok",
        "how_title": "Üç adımda başla",
        "how_sub": "Birkaç soru, iki fotoğraf ve planın hazır.",
        "steps": [
            ("Ne istediğini söyle", "Koçunu seç ve hedefini işaretle: boyun ve omuzlar, daha dik duruş ya da daha güçlü bir bel. Emin değilsen koçun bakar."),
            ("2 dakikalık kontrol", "Önden ve yandan iki fotoğraf çek. Ölçüm telefonunda yapılır; fotoğrafların telefonundan çıkmaz."),
            ("Planın hazır", "Ölçümüne göre 3 hareketle başlarsın. Haftanı tamamladıkça yeni hareketler açılır."),
        ],
        "result_title": "Hüküm değil, gözlem",
        "result_sub": "Sonuç ekranı ölçümün ne gördüğünü sade bir dille anlatır: ne görüldü, günlük hayatta ne zaman sık görülür ve planın neye öncelik veriyor. Puan ya da kırmızı uyarı yok.",
        "finding": {
            "tag": "Ölçümünden bir örnek", "name": "İleri baş duruşu",
            "obs": "Başın omuz hizasının biraz önünde duruyor.",
            "daily": "Uzun süre ekrana bakarken ya da masa başında otururken sık görülür.",
            "plan": "Planın boyun ve üst sırt çevresindeki hareketlere öncelik veriyor.",
            "strong_label": "Güçlü yanın", "strong": "Omuzların dengeli duruyor.",
        },
        "week_title": "Her gün biraz, her hafta bir adım",
        "week_sub": "Antrenman uzun olmak zorunda değil. Önemli olan düzen.",
        "week_points": [
            "<b>Tek bir hareket bile</b> günü doldurur. Ana antrenmanın tamamını yaparsan halkan altın olur.",
            "Haftada <b>5 dolu gün</b> hedef. 2 gün izin hakkın var; serin bozulmaz.",
            "Hafta tamamlanınca planın <b>bir adım ilerler</b> ve yeni hareketler açılır.",
            "<b>28 günde bir</b> kısa bir kontrolle neyin değiştiğini birlikte görürüz.",
        ],
        "week_example": "Örnek bir hafta",
        "legend": ["Dolu gün", "Ana antrenmanın tamamı", "İzin günü"],
        "packs_title": "Kısa molalar için paketler",
        "packs_sub": "Her paket 3 hareket ve 3–5 dakika. Ana planına ek olarak istediğin an aç. Hedefine uyan paket en üstte durur.",
        "packs": list(zip(PACK_IDS, ["Masa başı molası", "Boyun ve omuz", "Dik duruş", "Bel", "Sabah", "Akşam"])),
        "pack_meta": "3 hareket · 3–5 dk",
        "priority": "Önceliğin",
        "sens_title": "Hassas bir bölgen mi var?",
        "sens_sub": "Bölgeni seç ve nasıl çalışmak istediğini söyle. Dinlendirdiğin bölgeye dokunan hareketler plandan çıkar; hazır olunca Profil'den geri açarsın.",
        "regions": ["Boyun", "Omuz", "Sırt", "Bel", "Kalça", "Diz ve bacak", "El ve bilek", "Ayak ve bilek"],
        "gentle": "Nazik çalışabilirim", "rest": "Şimdilik dinlendirmem lazım",
        "coach_title": "Koçunla tanış",
        "coach_sub": "Elif ve Asım her hareketi 3D olarak gösterir, sesli yönlendirir ve sana eşlik eder. Burada deneyebilirsin.",
        "pick_coach": "Koçunu seç", "live": "Canlı göster", "try_moves": "Bir hareket dene",
        "moves": list(zip(MOVE_IDS, ['Shoulder Elevation', 'Glute Bridge', 'Cat-Cow'], ['Omuz elevasyon egzersizi üst trapez kaslarını çalıştırır. Dik bir pozisyonda dururken omuzlarınızı kulaklarınıza doğru çekin, tepe noktasında iki saniye bekleyip yavaşça aşağı bırakın.', 'Köprü egzersizi kalça ve hamstring kaslarını güçlendirir. Sırt üstü uzanın, dizlerinizi bükün. Kalçanızı havaya kaldırın, tepede beş saniye sıkın ve kontrollü bir şekilde indirin.', 'Kedi-İnek hareketi omurganızı mobilize eden harika bir egzersizdir. Emekleme pozisyonuna geçin. Nefes alırken sırtınızı düzleştirin ve belinizi çukurlaştırın bu inek pozisyonu. Nefes verirken sırtınızı kamburlaştırın ve belinizi düzleştirin, bu da kedi pozisyonu.'], ['Omuzlarınızı yukarı çekin. Tutun, iki. Yavaşça bırakın.', 'Kalçanızı yukarı kaldırın. Tepede sıkın, iki, üç, dört, beş. Yavaşça indirin.', 'Nefes alın, sırtı düzleştirip belinizi çukurlaştırın. Nefes verin, sırtı kamburlaştırın ve belinizi düzleştirip çenenizi göğsünüze yaklaştırın. Çok güzel, devam edin.'])),
        "coach_note": 'Rehberlik hareketi baştan anlatır; eşlikte koç hareketi seninle birlikte yapar ve sayar. Koçu parmağınla ya da fareyle döndürebilirsin. 3D görünüm yaklaşık 1–1,5 MB indirir.',
        "guide": 'Rehberlik', "company": 'Eşlik', "listen": 'Sesi dinle',
        "coach_names": ('Elif', 'Asım'),
        "loading": "Koç geliyor…", "load_error": "3D görünüm bu cihazda açılamadı.",
        "price_title": "Ücretsiz başla, istersen Pro'ya geç",
        "price_sub": "Ücretsiz sürüm süresiz. Pro'yu 7 gün ücretsiz deneyebilirsin; fiyatlar uygulamada gösterilir.",
        "free_name": "Ücretsiz", "free_sub": "Süresiz",
        "free": ["İlk kontrol ve ölçüm önizlemesi", "Sonucunun özeti ve güçlü yanın", "Ölçümüne göre 3 hareketlik planın", "Masa başı molası paketi", "Halkalar, seri ve rozetler"],
        "pro_sub": "7 gün ücretsiz dene",
        "pro": ["Her hafta açılan yeni hareketler", "28 günlük kontroller ve gelişim raporu", "Bütün paketler", "Ayrıntılı sonuçlar ve karşılaştırma"],
        "priv_title": "Fotoğrafların telefonunda kalır",
        "priv_sub": "Ölçüm yapay zekâyla doğrudan telefonunda yapılır. Fotoğrafların ve sonuçların sunucularımıza gönderilmez.",
        "privacy_points": ["<b>Ölçüm telefonda</b> yapılır, buluta fotoğraf gitmez.", "<b>Hesap açmadan</b> başlarsın; istersen sonra Google ya da Apple ile bağlarsın.", "<b>Reklam yok</b>; verilerini satmayız."],
        "priv_link": "Gizlilik politikasını oku",
        "faq_title": "Sık sorulanlar",
        "faq": [
            ("PosMetric tıbbi bir uygulama mı?", "Hayır. PosMetric bir fitness uygulamasıdır; tıbbi cihaz değildir ve sağlık hizmetinin yerine geçmez."),
            ("Hesap açmam gerekiyor mu?", "Hayır. Misafir olarak başlarsın. İstersen sonra Google ya da Apple hesabınla bağlarsın; kayıtların yerinde kalır."),
            ("Her gün ne kadar zaman ayırmalıyım?", "Tek bir hareket bile günü doldurur. Paketler 3–5 dakika sürer; ana antrenmanın uzunluğu planına göre değişir."),
            ("Hangi ekipman gerekiyor?", "Çoğu hareket için bir yatak ya da minder yeterli. Bazı hareketlerde duvar ya da bir çubuk kullanılır."),
            ("iPhone'da var mı?", "iOS sürümü hazırlanıyor. Şimdilik Android'de, Google Play'de."),
            ("Hangi dillerde kullanabilirim?", "Türkçe, İngilizce, Almanca ve İspanyolca."),
            ("Aboneliği nasıl iptal ederim?", 'Google Play → Ödemeler ve abonelikler → Abonelikler → PosMetric. Ayrıntılar <a href="/terms.html">Kullanım Şartları</a>\'nda.'),
        ],
        "end_title": "Bugün ilk kontrolünü yap",
        "end_sub": "İki fotoğraf, birkaç dakika. Gerisini koçunla birlikte yaparsın.",
    },
    "en": {
        "title": "PosMetric — Posture workouts with a personal coach",
        "desc": "Measure your posture with your phone camera and move every day with a short plan built around you. Your coach Emma or Jack joins every move. Start free.",
        "eyebrow": "Posture workouts · Personal coach",
        "h1": "Measure. Move. <span>Progress.</span>",
        "lead": "PosMetric measures your posture with your phone camera, builds a short workout plan around you and shows your progress honestly. Your coach joins you for every move.",
        "try_btn": "Try it in your browser",
        "try_hint": "Nothing to install · 30 seconds · The image stays on your device",
        "try_title": "Check your posture right now",
        "try_sub": "The same measurement as the app, in your browser. Your coach guides you into place by voice; once you're standing right, the measurement happens on its own.",
        "demo_caption": "A real measurement on a sample photo",
        "fine": "Start free · No account needed · No ads",
        "how_title": "Start in three steps",
        "how_sub": "A few questions, two photos and your plan is ready.",
        "steps": [
            ("Tell us what you want", "Pick your coach and choose a goal: neck and shoulders, standing taller or a stronger lower back. Not sure? Your coach takes a look."),
            ("A 2-minute check", "Take one photo from the front and one from the side. The measurement runs on your phone; your photos never leave it."),
            ("Your plan is ready", "You start with 3 movements based on your measurement. New movements unlock as you complete your weeks."),
        ],
        "result_title": "Observations, not verdicts",
        "result_sub": "Your results describe what the measurement sees in plain words: what was seen, when it's common in daily life and what your plan focuses on. No scores, no red warnings.",
        "finding": {
            "tag": "An example from a measurement", "name": "Forward head posture",
            "obs": "Your head sits a little in front of your shoulders.",
            "daily": "It's common when you look at a screen or sit at a desk for a long time.",
            "plan": "Your plan puts movements for your neck and upper back first.",
            "strong_label": "Your strength", "strong": "Your shoulders sit evenly.",
        },
        "week_title": "A little every day, one step every week",
        "week_sub": "Workouts don't have to be long. Showing up is what counts.",
        "week_points": [
            "<b>Even one movement</b> fills the day. Finish your whole main workout and your ring turns gold.",
            "The goal is <b>5 active days</b> a week. You get 2 rest days; your streak stays safe.",
            "When the week is done, your plan <b>moves one step forward</b> and new movements unlock.",
            "<b>Every 28 days</b> a short check shows what has changed.",
        ],
        "week_example": "An example week",
        "legend": ["Active day", "Whole main workout", "Rest day"],
        "packs_title": "Packs for short breaks",
        "packs_sub": "Each pack is 3 movements and 3–5 minutes. Open one whenever you like, on top of your main plan. The pack that matches your goal sits at the top.",
        "packs": list(zip(PACK_IDS, ["Desk break", "Neck and shoulders", "Stand tall", "Lower back", "Morning", "Evening"])),
        "pack_meta": "3 movements · 3–5 min",
        "priority": "Your priority",
        "sens_title": "Got a sensitive area?",
        "sens_sub": "Pick the area and tell us how you'd like to train. Movements that involve an area you're resting are taken out of your plan; turn them back on in Profile when you're ready.",
        "regions": ["Neck", "Shoulder", "Upper back", "Lower back", "Hip", "Knee and leg", "Hand and wrist", "Foot and ankle"],
        "gentle": "I can go gently", "rest": "I need to rest it for now",
        "coach_title": "Meet your coach",
        "coach_sub": "Emma and Jack show every movement in 3D, guide you with their voice and keep you company. Try them out here.",
        "pick_coach": "Pick your coach", "live": "Show live", "try_moves": "Try a movement",
        "moves": list(zip(MOVE_IDS, ['Shoulder Shrugs', 'Glute Bridge', 'Cat-Cow'], ['The shoulder elevation exercise works the upper trapezius muscles. While standing tall, shrug your shoulders towards your ears, hold for two seconds at the top, and slowly release down.', 'The bridge exercise strengthens the glute and hamstring muscles. Lie on your back with your knees bent. Lift your hips into the air, squeeze at the top for five seconds, and lower with control.', 'The Cat-Cow is a great exercise to mobilize your spine. Get into a quadruped position. As you inhale, flatten your back and drop your belly; this is the cow pose. As you exhale, arch your back and tuck your pelvis; this is the cat pose.'], ['Pull your shoulders up. Hold for two. Slowly release.', 'Lift your hips up. Squeeze at the top, two, three, four, five. Lower slowly.', 'Inhale, flatten your back and drop your belly. Exhale, arch your back, tuck your pelvis, and bring your chin towards your chest. Very good, keep going.'])),
        "coach_note": 'Guidance explains the movement from the start; in company mode your coach does the movement with you and counts along. Drag to turn the coach around. The 3D view downloads about 1–1.5 MB.',
        "guide": 'Guidance', "company": 'Company', "listen": 'Listen',
        "coach_names": ('Emma', 'Jack'),
        "loading": "Your coach is on the way…", "load_error": "The 3D view couldn't open on this device.",
        "price_title": "Start free, go Pro if you like",
        "price_sub": "The free version never expires. Try Pro free for 7 days; prices are shown in the app.",
        "free_name": "Free", "free_sub": "No time limit",
        "free": ["Your first check and measurement preview", "A summary of your results and your strength", "A 3-movement plan based on your measurement", "The Desk break pack", "Rings, streaks and badges"],
        "pro_sub": "Try 7 days free",
        "pro": ["New movements that unlock every week", "28-day checks and a progress report", "All packs", "Detailed results and comparisons"],
        "priv_title": "Your photos stay on your phone",
        "priv_sub": "The measurement runs with on-device AI. Your photos and results are never sent to our servers.",
        "privacy_points": ["<b>Measured on your phone</b>; no photos go to the cloud.", "<b>No account needed</b> to start; link Google or Apple later if you like.", "<b>No ads</b>; we don't sell your data."],
        "priv_link": "Read the privacy policy",
        "faq_title": "Questions",
        "faq": [
            ("Is PosMetric a medical app?", "No. PosMetric is a fitness app; it is not a medical device and does not replace professional health care."),
            ("Do I need an account?", "No. You start as a guest. You can link your Google or Apple account later; your records stay where they are."),
            ("How much time do I need each day?", "Even one movement fills the day. Packs take 3–5 minutes; your main workout's length depends on your plan."),
            ("What equipment do I need?", "A bed or a mat is enough for most movements. Some use a wall or a stick."),
            ("Is it on iPhone?", "The iOS version is on its way. For now PosMetric is on Android, on Google Play."),
            ("Which languages are supported?", "English, Turkish, German and Spanish."),
            ("How do I cancel my subscription?", 'Google Play → Payments &amp; subscriptions → Subscriptions → PosMetric. See the <a href="/en/terms.html">Terms of Use</a> for details.'),
        ],
        "end_title": "Do your first check today",
        "end_sub": "Two photos, a few minutes. Your coach takes it from there with you.",
    },
    "de": {
        "title": "PosMetric — Haltungstraining mit persönlichem Coach",
        "desc": "Miss deine Haltung mit der Handykamera und beweg dich jeden Tag mit einem kurzen Plan, der zu dir passt. Dein Coach Anna oder Max ist bei jeder Übung dabei. Kostenlos starten.",
        "eyebrow": "Haltungstraining · Persönlicher Coach",
        "h1": "Messen. Bewegen. <span>Dranbleiben.</span>",
        "lead": "PosMetric misst deine Haltung mit deiner Handykamera, stellt einen kurzen Trainingsplan für dich zusammen und zeigt deine Entwicklung ehrlich. Dein Coach ist bei jeder Übung dabei.",
        "try_btn": "Im Browser ausprobieren",
        "try_hint": "Keine Installation · 30 Sekunden · Das Bild bleibt auf deinem Gerät",
        "try_title": "Sieh dir deine Haltung jetzt an",
        "try_sub": "Dieselbe Messung wie in der App, in deinem Browser. Dein Coach leitet dich mit der Stimme an die richtige Stelle; sobald du richtig stehst, startet die Messung von selbst.",
        "demo_caption": "Echte Messung an einem Beispielfoto",
        "fine": "Kostenlos starten · Kein Konto nötig · Keine Werbung",
        "how_title": "In drei Schritten loslegen",
        "how_sub": "Ein paar Fragen, zwei Fotos und dein Plan steht.",
        "steps": [
            ("Sag, was du willst", "Wähl deinen Coach und dein Ziel: Nacken und Schultern, aufrechter stehen oder ein stärkerer unterer Rücken. Unsicher? Dein Coach schaut für dich."),
            ("2-Minuten-Check", "Mach ein Foto von vorne und eins von der Seite. Die Messung läuft auf deinem Handy; deine Fotos verlassen es nicht."),
            ("Dein Plan steht", "Du startest mit 3 Übungen, die zu deiner Messung passen. Mit jeder geschafften Woche kommen neue dazu."),
        ],
        "result_title": "Beobachtungen statt Urteile",
        "result_sub": "Dein Ergebnis beschreibt in einfachen Worten, was die Messung sieht: was zu sehen ist, wann das im Alltag oft vorkommt und worauf dein Plan setzt. Keine Punkte, keine roten Warnungen.",
        "finding": {
            "tag": "Ein Beispiel aus einer Messung", "name": "Kopf vor der Schulterlinie",
            "obs": "Dein Kopf steht etwas vor der Schulterlinie.",
            "daily": "Das sieht man oft, wenn man lange auf einen Bildschirm schaut oder am Schreibtisch sitzt.",
            "plan": "Dein Plan setzt Übungen für Nacken und oberen Rücken an erste Stelle.",
            "strong_label": "Deine Stärke", "strong": "Deine Schultern stehen gleichmäßig.",
        },
        "week_title": "Jeden Tag ein bisschen, jede Woche ein Schritt",
        "week_sub": "Training muss nicht lang sein. Entscheidend ist, dranzubleiben.",
        "week_points": [
            "<b>Schon eine Übung</b> füllt den Tag. Schaffst du dein ganzes Haupttraining, wird dein Ring golden.",
            "Ziel sind <b>5 aktive Tage</b> pro Woche. 2 Ruhetage sind drin; deine Serie bleibt bestehen.",
            "Ist die Woche geschafft, geht dein Plan <b>einen Schritt weiter</b> und neue Übungen kommen dazu.",
            "<b>Alle 28 Tage</b> zeigt ein kurzer Check, was sich verändert hat.",
        ],
        "week_example": "Eine Beispielwoche",
        "legend": ["Aktiver Tag", "Ganzes Haupttraining", "Ruhetag"],
        "packs_title": "Pakete für kurze Pausen",
        "packs_sub": "Jedes Paket hat 3 Übungen und dauert 3–5 Minuten. Öffne es jederzeit zusätzlich zu deinem Hauptplan. Das Paket zu deinem Ziel steht ganz oben.",
        "packs": list(zip(PACK_IDS, ["Schreibtischpause", "Nacken und Schultern", "Aufrecht", "Unterer Rücken", "Morgen", "Abend"])),
        "pack_meta": "3 Übungen · 3–5 Min.",
        "priority": "Deine Priorität",
        "sens_title": "Gibt es einen empfindlichen Bereich?",
        "sens_sub": "Wähl den Bereich und sag, wie du trainieren möchtest. Übungen für einen Bereich, der gerade ruht, kommen aus dem Plan; im Profil schaltest du sie wieder ein, wenn du so weit bist.",
        "regions": ["Nacken", "Schulter", "Oberer Rücken", "Unterer Rücken", "Hüfte", "Knie und Bein", "Hand und Handgelenk", "Fuß und Sprunggelenk"],
        "gentle": "Ich kann sanft trainieren", "rest": "Ich muss sie vorerst schonen",
        "coach_title": "Lern deinen Coach kennen",
        "coach_sub": "Anna und Max zeigen jede Übung in 3D, leiten dich mit ihrer Stimme an und begleiten dich. Probier es hier aus.",
        "pick_coach": "Wähl deinen Coach", "live": "Live zeigen", "try_moves": "Probier eine Übung",
        "moves": list(zip(MOVE_IDS, ['Schulterheben', 'Gesäßbrücke', 'Katze-Kuh'], ['Diese Übung trainiert den oberen Trapezius. Im Stehen die Schultern in Richtung der Ohren hochziehen, zwei Sekunden oben halten und langsam wieder nach unten absenken.', 'Die Gesäßbrücke stärkt die Gesäß- und hintere Oberschenkelmuskulatur. Legen Sie sich auf den Rücken, Knie angewinkelt. Heben Sie das Becken an, spannen Sie die Muskulatur fünf Sekunden lang oben an und senken Sie das Becken kontrolliert ab.', 'Die Katze-Kuh-Übung ist hervorragend zur Mobilisation der Wirbelsäule. Kommen Sie in den Vierfüßlerstand. Beim Einatmen flachen Sie Ihren Rücken ab und lassen den Bauch sinken – dies ist die Kuh-Position. Beim Ausatmen machen Sie einen runden Rücken und kippen Ihr Becken – dies ist die Katze-Position.'], ['Schultern hochziehen. Halten, zwei. Langsam absenken.', 'Becken anheben. Oben anspannen, zwei, drei, vier, fünf. Langsam absenken.', 'Einatmen, den Rücken abflachen und den Bauch sinken lassen. Ausatmen, den Rücken runden, das Becken kippen und das Kinn zur Brust führen. Sehr gut, weiter so.'])),
        "coach_note": 'Die Anleitung erklärt die Übung von Anfang an; bei der Begleitung macht dein Coach die Übung mit dir und zählt mit. Zieh mit dem Finger oder der Maus, um den Coach zu drehen. Die 3D-Ansicht lädt etwa 1–1,5 MB.',
        "guide": 'Anleitung', "company": 'Begleitung', "listen": 'Anhören',
        "coach_names": ('Anna', 'Max'),
        "loading": "Dein Coach kommt…", "load_error": "Die 3D-Ansicht lässt sich auf diesem Gerät nicht öffnen.",
        "price_title": "Kostenlos starten, Pro wenn du willst",
        "price_sub": "Die kostenlose Version ist unbefristet. Pro kannst du 7 Tage kostenlos testen; die Preise siehst du in der App.",
        "free_name": "Kostenlos", "free_sub": "Unbefristet",
        "free": ["Dein erster Check mit Messvorschau", "Eine Zusammenfassung deines Ergebnisses und deine Stärke", "Ein Plan mit 3 Übungen passend zu deiner Messung", "Das Paket Schreibtischpause", "Ringe, Serien und Abzeichen"],
        "pro_sub": "7 Tage kostenlos testen",
        "pro": ["Jede Woche neue Übungen", "28-Tage-Checks und Fortschrittsbericht", "Alle Pakete", "Ausführliche Ergebnisse und Vergleiche"],
        "priv_title": "Deine Fotos bleiben auf deinem Handy",
        "priv_sub": "Die Messung läuft mit KI direkt auf deinem Gerät. Fotos und Ergebnisse werden nicht an unsere Server gesendet.",
        "privacy_points": ["<b>Gemessen auf dem Handy</b>; keine Fotos in der Cloud.", "<b>Ohne Konto</b> starten; Google oder Apple kannst du später verknüpfen.", "<b>Keine Werbung</b>; wir verkaufen deine Daten nicht."],
        "priv_link": "Datenschutzerklärung lesen",
        "faq_title": "Häufige Fragen",
        "faq": [
            ("Ist PosMetric eine medizinische App?", "Nein. PosMetric ist eine Fitness-App; sie ist kein Medizinprodukt und ersetzt keine ärztliche Beratung."),
            ("Brauche ich ein Konto?", "Nein. Du startest als Gast. Später kannst du dein Google- oder Apple-Konto verknüpfen; deine Einträge bleiben erhalten."),
            ("Wie viel Zeit brauche ich pro Tag?", "Schon eine Übung füllt den Tag. Pakete dauern 3–5 Minuten; wie lang dein Haupttraining ist, hängt von deinem Plan ab."),
            ("Welche Ausrüstung brauche ich?", "Für die meisten Übungen reicht ein Bett oder eine Matte. Manche nutzen eine Wand oder einen Stab."),
            ("Gibt es PosMetric fürs iPhone?", "Die iOS-Version ist in Arbeit. Bis dahin gibt es PosMetric für Android bei Google Play."),
            ("In welchen Sprachen gibt es die App?", "Deutsch, Englisch, Türkisch und Spanisch."),
            ("Wie kündige ich mein Abo?", 'Google Play → Zahlungen und Abos → Abos → PosMetric. Details findest du in den <a href="/de/terms.html">Nutzungsbedingungen</a>.'),
        ],
        "end_title": "Mach heute deinen ersten Check",
        "end_sub": "Zwei Fotos, ein paar Minuten. Den Rest machst du zusammen mit deinem Coach.",
    },
    "es": {
        "title": "PosMetric — Entrenamiento postural con coach personal",
        "desc": "Mide tu postura con la cámara del móvil y muévete cada día con un plan corto hecho para ti. Tu coach Lucía o Carlos te acompaña en cada movimiento. Empieza gratis.",
        "eyebrow": "Entrenamiento postural · Coach personal",
        "h1": "Mide. Muévete. <span>Avanza.</span>",
        "lead": "PosMetric mide tu postura con la cámara del móvil, arma un plan de entrenamiento corto para ti y te muestra tu evolución con honestidad. Tu coach te acompaña en cada movimiento.",
        "try_btn": "Pruébalo en tu navegador",
        "try_hint": "Sin instalar nada · 30 segundos · La imagen se queda en tu dispositivo",
        "try_title": "Mira tu postura ahora mismo",
        "try_sub": "La misma medición que en la app, en tu navegador. Tu coach te guía con la voz hasta tu sitio y, cuando estás bien colocado, la medición se hace sola.",
        "demo_caption": "Medición real en una foto de ejemplo",
        "fine": "Empieza gratis · Sin cuenta · Sin anuncios",
        "how_title": "Empieza en tres pasos",
        "how_sub": "Unas preguntas, dos fotos y tu plan está listo.",
        "steps": [
            ("Dinos qué quieres", "Elige tu coach y tu objetivo: cuello y hombros, una postura más erguida o una zona lumbar más fuerte. ¿No lo sabes? Tu coach lo mira por ti."),
            ("Revisión de 2 minutos", "Haz una foto de frente y otra de lado. La medición se hace en tu móvil; tus fotos no salen de él."),
            ("Tu plan está listo", "Empiezas con 3 movimientos según tu medición. Al completar tus semanas se abren movimientos nuevos."),
        ],
        "result_title": "Observaciones, no juicios",
        "result_sub": "Tus resultados cuentan con palabras sencillas lo que ve la medición: qué se vio, cuándo es frecuente en el día a día y a qué da prioridad tu plan. Sin puntuaciones ni avisos en rojo.",
        "finding": {
            "tag": "Un ejemplo de una medición", "name": "Cabeza adelantada",
            "obs": "Tu cabeza está un poco por delante de la línea de los hombros.",
            "daily": "Es frecuente cuando pasas mucho rato mirando una pantalla o frente al escritorio.",
            "plan": "Tu plan da prioridad a los movimientos de cuello y parte alta de la espalda.",
            "strong_label": "Tu punto fuerte", "strong": "Tus hombros están equilibrados.",
        },
        "week_title": "Un poco cada día, un paso cada semana",
        "week_sub": "Entrenar no tiene que ser largo. Lo que cuenta es la constancia.",
        "week_points": [
            "<b>Un solo movimiento</b> ya llena el día. Si completas tu entrenamiento principal, tu anillo se vuelve dorado.",
            "El objetivo son <b>5 días activos</b> por semana. Tienes 2 días de descanso; tu racha sigue en pie.",
            "Al completar la semana, tu plan <b>avanza un paso</b> y se abren movimientos nuevos.",
            "<b>Cada 28 días</b> una revisión corta muestra qué ha cambiado.",
        ],
        "week_example": "Una semana de ejemplo",
        "legend": ["Día activo", "Entrenamiento principal completo", "Día de descanso"],
        "packs_title": "Paquetes para pausas cortas",
        "packs_sub": "Cada paquete tiene 3 movimientos y dura 3–5 minutos. Ábrelo cuando quieras, además de tu plan principal. El paquete de tu objetivo queda arriba.",
        "packs": list(zip(PACK_IDS, ["Pausa de escritorio", "Cuello y hombros", "Postura erguida", "Zona lumbar", "Mañana", "Noche"])),
        "pack_meta": "3 movimientos · 3–5 min",
        "priority": "Tu prioridad",
        "sens_title": "¿Tienes una zona sensible?",
        "sens_sub": "Elige la zona y dinos cómo quieres entrenar. Los movimientos que usan una zona en descanso salen de tu plan; vuelve a activarlos en Perfil cuando quieras.",
        "regions": ["Cuello", "Hombro", "Espalda", "Zona lumbar", "Cadera", "Rodilla y pierna", "Mano y muñeca", "Pie y tobillo"],
        "gentle": "Puedo trabajar con suavidad", "rest": "Necesito que descanse por ahora",
        "coach_title": "Conoce a tu coach",
        "coach_sub": "Lucía y Carlos muestran cada movimiento en 3D, te guían con su voz y te acompañan. Pruébalos aquí.",
        "pick_coach": "Elige tu coach", "live": "Ver en vivo", "try_moves": "Prueba un movimiento",
        "moves": list(zip(MOVE_IDS, ['Elevación de hombros', 'Puente de glúteos', 'Gato-vaca'], ['El ejercicio de elevación de hombros trabaja los músculos del trapecio superior. Estando de pie, encoja los hombros hacia las orejas, mantenga durante dos segundos en la parte superior y baje lentamente.', 'El ejercicio de puente fortalece los glúteos y los músculos isquiotibiales. Acuéstese boca arriba con las rodillas dobladas. Levante las caderas en el aire, apriete en la parte superior durante cinco segundos y baje con control.', 'El Gato-Vaca es un excelente ejercicio para movilizar la columna vertebral. Póngase en posición cuadrúpeda. Al inhalar, aplane la espalda y baje el vientre; esta es la postura de la vaca. Al exhalar, arquee la espalda y meta la pelvis; esta es la postura del gato.'], ['Levante los hombros. Mantenga durante dos. Baje lentamente.', 'Levante las caderas hacia arriba. Apriete en la parte superior, dos, tres, cuatro, cinco. Baje lentamente.', 'Inhale, aplane la espalda y baje el vientre. Exhale, arquee la espalda, meta la pelvis y lleve la barbilla hacia el pecho. Muy bien, continúe.'])),
        "coach_note": 'La guía explica el movimiento desde el principio; en compañía tu coach hace el movimiento contigo y cuenta. Arrastra para girar al coach. La vista 3D descarga unos 1–1,5 MB.',
        "guide": 'Guía', "company": 'Compañía', "listen": 'Escuchar',
        "coach_names": ('Lucía', 'Carlos'),
        "loading": "Tu coach está llegando…", "load_error": "La vista 3D no se pudo abrir en este dispositivo.",
        "price_title": "Empieza gratis, pásate a Pro si quieres",
        "price_sub": "La versión gratuita no caduca. Prueba Pro gratis durante 7 días; los precios se muestran en la app.",
        "free_name": "Gratis", "free_sub": "Sin límite de tiempo",
        "free": ["Tu primera revisión y la vista previa de la medición", "Un resumen de tus resultados y tu punto fuerte", "Un plan de 3 movimientos según tu medición", "El paquete Pausa de escritorio", "Anillos, rachas e insignias"],
        "pro_sub": "Pruébalo 7 días gratis",
        "pro": ["Movimientos nuevos cada semana", "Revisiones cada 28 días e informe de evolución", "Todos los paquetes", "Resultados detallados y comparaciones"],
        "priv_title": "Tus fotos se quedan en tu móvil",
        "priv_sub": "La medición se hace con IA directamente en tu dispositivo. Tus fotos y resultados no se envían a nuestros servidores.",
        "privacy_points": ["<b>Se mide en tu móvil</b>; ninguna foto va a la nube.", "<b>Sin cuenta</b> para empezar; si quieres, vincula Google o Apple después.", "<b>Sin anuncios</b>; no vendemos tus datos."],
        "priv_link": "Leer la política de privacidad",
        "faq_title": "Preguntas frecuentes",
        "faq": [
            ("¿PosMetric es una app médica?", "No. PosMetric es una app de fitness; no es un dispositivo médico y no sustituye la atención sanitaria profesional."),
            ("¿Necesito una cuenta?", "No. Empiezas como invitado. Más adelante puedes vincular tu cuenta de Google o Apple; tus registros se mantienen."),
            ("¿Cuánto tiempo necesito al día?", "Un solo movimiento ya llena el día. Los paquetes duran 3–5 minutos; la duración del entrenamiento principal depende de tu plan."),
            ("¿Qué material necesito?", "Para la mayoría de los movimientos basta una cama o una esterilla. Algunos usan una pared o un palo."),
            ("¿Está disponible en iPhone?", "La versión para iOS está en camino. Por ahora PosMetric está en Android, en Google Play."),
            ("¿En qué idiomas está?", "Español, inglés, turco y alemán."),
            ("¿Cómo cancelo mi suscripción?", 'Google Play → Pagos y suscripciones → Suscripciones → PosMetric. Más detalles en los <a href="/es/terms.html">Términos de uso</a>.'),
        ],
        "end_title": "Haz hoy tu primera revisión",
        "end_sub": "Dos fotos y unos minutos. Lo demás lo haces junto a tu coach.",
    },
}

# ---------------------------------------------------------------- Hukuki ve bilgi sayfaları

LEGAL = {"tr": {}, "en": {}, "de": {}, "es": {}}

LEGAL["tr"]["privacy"] = {
    "title": "Gizlilik Politikası", "date": "8 Ekim 2026",
    "desc": "PosMetric hangi verileri işler, hangileri telefonunuzda kalır ve haklarınız nelerdir.",
    "body": """
<div class="callout key"><p><strong>Temel ilke:</strong> Duruş ölçümü telefonunuzda yapılır. Fotoğraflarınız, ölçüm sonuçlarınız ve antrenman verileriniz sunucularımıza gönderilmez.</p></div>
<div class="callout"><p><strong>Not:</strong> PosMetric bir fitness uygulamasıdır; tıbbi cihaz değildir.</p></div>

<h2>1. Telefonunuzda kalan veriler</h2>
<p>Aşağıdaki veriler yalnızca telefonunuzdaki uygulama alanında tutulur ve sunucularımıza gönderilmez:</p>
<ul>
<li><strong>Fotoğraflar:</strong> Ölçüm için çektiğiniz ya da galeriden seçtiğiniz fotoğraflar.</li>
<li><strong>Ölçüm sonuçları:</strong> Vücut noktaları, açı hesapları, gözlemler ve geçmiş ölçümleriniz.</li>
<li><strong>Plan ayarları:</strong> Hedefiniz, hassas ya da dinlendirdiğiniz bölgeler, hatırlatma saatiniz ve koç seçiminiz.</li>
<li><strong>Antrenman kayıtları:</strong> Yaptığınız hareketler, dolu günler, seri, rozetler ve planınızın ilerleyişi.</li>
</ul>
<p><strong>Cihaz yedeği:</strong> Telefonunuzun yedekleme özelliği açıksa (Google yedeği ya da iCloud), işletim sistemi bu verileri kendi hesabınızdaki yedeğe alabilir. Bu yedekler sizin hesabınızdadır; biz erişemeyiz.</p>

<h2>2. İşlenen veriler</h2>
<h3>2.1. Kimlik ve hesap</h3>
<p>Uygulama ilk açıldığında size Firebase Authentication üzerinden <strong>anonim bir kullanıcı kimliği</strong> atanır; bunun için ad ya da e-posta istenmez. Google veya Apple ile giriş yaparsanız <strong>e-posta adresiniz</strong>, <strong>görünen adınız</strong> ve <strong>kullanıcı kimliğiniz</strong> kimlik doğrulama için işlenir ve anonim kimliğiniz bu girişe bağlanır.</p>
<h3>2.2. Ücretsiz kullanım hakkı</h3>
<p>Ücretsiz ölçüm hakkının kötüye kullanılmasını önlemek için Firebase Firestore'da yalnızca şunlar tutulur:</p>
<ul>
<li>Kullanıcı kimliğinize bağlı <strong>ölçüm sayısı</strong> ve son ölçüm zamanı.</li>
<li>Cihazınızdan üretilen, kişiyi tanımlamayan <strong>anonim bir cihaz özeti</strong> (SHA-256) ve bu cihazdaki ölçüm sayısı.</li>
</ul>
<p>Bu kayıtlar fotoğraf, ölçüm sonucu ya da antrenman verisi içermez.</p>
<h3>2.3. Geri bildirim</h3>
<p>Uygulamadaki geri bildirim formunu kullanırsanız, mesajınız ile uygulama sürümü ve cihaz bilgisi (model, işletim sistemi, ekran çözünürlüğü) Firestore'a kaydedilir ve destek e-posta adresimize iletilir.</p>
<h3>2.4. Abonelik</h3>
<p>PosMetric Pro satın alımları Google Play Faturalandırma üzerinden (iOS sürümü yayımlandığında App Store üzerinden) yapılır. Abonelik durumunuz RevenueCat aracılığıyla doğrulanır; bunun için RevenueCat'e uygulamadaki kullanıcı kimliğiniz iletilir. Ödeme bilgilerinizi biz görmeyiz.</p>
<h3>2.5. Kullanım, hata ve hizmet verileri</h3>
<ul>
<li><strong>Firebase Analytics:</strong> Ekran görüntülemeleri, oturum süreleri, genel cihaz bilgileri ve anonim etkileşim olayları (ör. ölçümü tamamlama, antrenmana başlama ve bitirme). Fotoğraf, ölçüm sonucu ya da sizi doğrudan tanımlayan bilgi içermez.</li>
<li><strong>Reklam kimliği:</strong> Firebase Analytics, cihazın reklam kimliğini yalnızca kullanım analizi için kullanabilir. Uygulamada reklam gösterilmez.</li>
<li><strong>Firebase Crashlytics:</strong> Uygulama çöktüğünde hata raporu, cihaz modeli, işletim sistemi, uygulama sürümü ve kuruluma bağlı teknik bir tanımlayıcı.</li>
<li><strong>Firebase App Check:</strong> Uygulamanın orijinal hâliyle gerçek bir cihazda çalıştığını doğrulayan bütünlük kontrolü.</li>
<li><strong>Firebase Remote Config ve Storage:</strong> Uygulama ayarlarının güncellenmesi ve koç ses paketlerinin indirilmesi. Bu sırada kuruluma bağlı teknik bir tanımlayıcı ve IP adresi işlenir.</li>
</ul>

<h2>3. İzinler</h2>
<ul>
<li><strong>Kamera:</strong> Yalnızca ölçüm fotoğrafı çekmek için.</li>
<li><strong>Fotoğraflar / galeri:</strong> Ölçüm için galeriden fotoğraf seçebilmeniz için.</li>
<li><strong>Bildirimler (isteğe bağlı):</strong> Seçtiğiniz saatte günlük hatırlatma için. Hatırlatmalar telefonunuzda zamanlanır.</li>
</ul>

<h2>4. Veri paylaşımı</h2>
<p>Kişisel verilerinizi satmayız, kiralamayız ve pazarlama amacıyla paylaşmayız. Veriler yalnızca hizmeti sunmak için kullandığımız şu hizmet sağlayıcılar tarafından işlenir:</p>
<ul>
<li><strong>Google Firebase:</strong> Authentication, Firestore, Analytics, Crashlytics, App Check, Remote Config, Storage. <a href="https://policies.google.com/privacy">policies.google.com/privacy</a></li>
<li><strong>RevenueCat:</strong> Abonelik doğrulama. <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a></li>
<li><strong>Google Play Faturalandırma ve Apple App Store:</strong> Ödeme işlemleri.</li>
<li><strong>Yasal zorunluluk:</strong> Yürürlükteki yasaların gerektirdiği durumlarda.</li>
</ul>
<p>Bu hizmet sağlayıcılar verileri Türkiye ve Avrupa Ekonomik Alanı dışında, özellikle ABD'de işleyebilir.</p>

<h2>5. Veri güvenliği</h2>
<ul>
<li>Telefondaki veriler işletim sisteminin uygulama korumalı alanında (sandbox) saklanır.</li>
<li>Sunuculara giden tüm veriler TLS ile şifrelenir.</li>
<li>Yalnızca gereken en az veri toplanır.</li>
<li>Uygulamayı kaldırdığınızda telefondaki tüm uygulama verileri silinir.</li>
</ul>

<h2>6. Haklarınız ve veri silme</h2>
<ul>
<li><strong>Hesap ve veri silme:</strong> Uygulamada Profil &gt; Hesabı Sil ile hesabınızı ve sunucudaki hesap kayıtlarınızı silebilirsiniz. Uygulamaya erişemiyorsanız <a href="/delete-account.html">hesap silme sayfasındaki</a> adımları izleyin.</li>
<li><strong>Anonim cihaz özeti:</strong> Kişiyi tanımlamadığı için hesap silindikten sonra da ücretsiz hak kontrolü amacıyla saklanabilir.</li>
<li><strong>Diğer haklar:</strong> KVKK ve GDPR kapsamında verilerinize erişme, düzeltme, silme, işlemeye itiraz etme ve şikâyette bulunma haklarınızı kullanmak için bize yazabilirsiniz.</li>
</ul>

<h2>7. Yaş sınırı</h2>
<p>PosMetric 18 yaş ve üzeri kullanıcılar için tasarlanmıştır. 18 yaşından küçüklerden bilerek kişisel veri toplamayız; fark edersek sileriz.</p>

<h2>8. Değişiklikler</h2>
<p>Bu politika zaman zaman güncellenebilir. Güncel sürüm her zaman bu sayfada yayımlanır.</p>

<h2>9. İletişim</h2>
<p>Veri sorumlusu: FArk Studio · E-posta: <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

LEGAL["en"]["privacy"] = {
    "title": "Privacy Policy", "date": "October 8, 2026",
    "desc": "What data PosMetric processes, what stays on your phone and what your rights are.",
    "body": """
<div class="callout key"><p><strong>Core principle:</strong> Posture measurement runs on your phone. Your photos, measurement results and workout data are never sent to our servers.</p></div>
<div class="callout"><p><strong>Note:</strong> PosMetric is a fitness app, not a medical device.</p></div>

<h2>1. Data that stays on your phone</h2>
<p>The following data is kept only in the app's storage on your phone and is never sent to our servers:</p>
<ul>
<li><strong>Photos:</strong> Photos you take or pick from your gallery for a measurement.</li>
<li><strong>Measurement results:</strong> Body landmarks, angle calculations, observations and your past measurements.</li>
<li><strong>Plan settings:</strong> Your goal, sensitive or resting areas, reminder time and coach choice.</li>
<li><strong>Workout records:</strong> The movements you do, active days, streaks, badges and your plan's progress.</li>
</ul>
<p><strong>Device backup:</strong> If your phone's backup is turned on (Google backup or iCloud), the operating system may include this data in a backup in your own account. These backups belong to your account; we cannot access them.</p>

<h2>2. Data we process</h2>
<h3>2.1. Identity and account</h3>
<p>When you first open the app, Firebase Authentication assigns you an <strong>anonymous user ID</strong>; no name or email is needed. If you sign in with Google or Apple, your <strong>email address</strong>, <strong>display name</strong> and <strong>user ID</strong> are processed for sign-in, and your anonymous ID is linked to that sign-in.</p>
<h3>2.2. Free allowance</h3>
<p>To prevent abuse of the free measurement allowance, only the following is stored in Firebase Firestore:</p>
<ul>
<li>The <strong>number of measurements</strong> and the time of your last measurement, linked to your user ID.</li>
<li>An <strong>anonymous device hash</strong> (SHA-256) that does not identify you, and the number of measurements on that device.</li>
</ul>
<p>These records contain no photos, measurement results or workout data.</p>
<h3>2.3. Feedback</h3>
<p>If you use the in-app feedback form, your message together with the app version and device information (model, OS, screen resolution) is stored in Firestore and forwarded to our support email.</p>
<h3>2.4. Subscription</h3>
<p>PosMetric Pro is purchased through Google Play Billing (and through the App Store once the iOS version is released). Your subscription status is verified via RevenueCat, which receives your in-app user ID for this purpose. We never see your payment details.</p>
<h3>2.5. Usage, crash and service data</h3>
<ul>
<li><strong>Firebase Analytics:</strong> Screen views, session lengths, general device information and anonymous interaction events (e.g. completing a measurement, starting or finishing a workout). No photos, measurement results or information that directly identifies you.</li>
<li><strong>Advertising ID:</strong> Firebase Analytics may use the device advertising ID for usage analytics only. The app shows no ads.</li>
<li><strong>Firebase Crashlytics:</strong> When the app crashes: a crash report, device model, OS, app version and a technical identifier linked to the installation.</li>
<li><strong>Firebase App Check:</strong> An integrity check that verifies the app is running unmodified on a genuine device.</li>
<li><strong>Firebase Remote Config and Storage:</strong> Updating app settings and downloading coach voice packs. An installation identifier and your IP address are processed in the process.</li>
</ul>

<h2>3. Permissions</h2>
<ul>
<li><strong>Camera:</strong> Only to take measurement photos.</li>
<li><strong>Photos / gallery:</strong> So you can pick a photo for a measurement.</li>
<li><strong>Notifications (optional):</strong> For a daily reminder at the time you choose. Reminders are scheduled on your phone.</li>
</ul>

<h2>4. Data sharing</h2>
<p>We do not sell, rent or share your personal data for marketing. Data is processed only by the following service providers we use to run the service:</p>
<ul>
<li><strong>Google Firebase:</strong> Authentication, Firestore, Analytics, Crashlytics, App Check, Remote Config, Storage. <a href="https://policies.google.com/privacy">policies.google.com/privacy</a></li>
<li><strong>RevenueCat:</strong> Subscription verification. <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a></li>
<li><strong>Google Play Billing and Apple App Store:</strong> Payment processing.</li>
<li><strong>Legal requirements:</strong> Where required by applicable law.</li>
</ul>
<p>These providers may process data outside Türkiye and the European Economic Area, in particular in the United States.</p>

<h2>5. Data security</h2>
<ul>
<li>On-device data is kept in the operating system's app sandbox.</li>
<li>All data sent to servers is encrypted with TLS.</li>
<li>We collect only the minimum data needed.</li>
<li>Uninstalling the app deletes all app data on your phone.</li>
</ul>

<h2>6. Your rights and data deletion</h2>
<ul>
<li><strong>Account and data deletion:</strong> Use Profile &gt; Delete Account in the app to delete your account and its server records. If you cannot access the app, follow the steps on our <a href="/en/delete-account.html">account deletion page</a>.</li>
<li><strong>Anonymous device hash:</strong> Because it does not identify you, it may be kept after account deletion to enforce the free allowance.</li>
<li><strong>Other rights:</strong> Under the GDPR and Turkish data protection law (KVKK) you can ask to access, correct or delete your data, object to processing or lodge a complaint. Just write to us.</li>
</ul>

<h2>7. Age requirement</h2>
<p>PosMetric is intended for users aged 18 and over. We do not knowingly collect personal data from anyone under 18; if we become aware of such data, we delete it.</p>

<h2>8. Changes</h2>
<p>This policy may be updated from time to time. The current version is always published on this page.</p>

<h2>9. Contact</h2>
<p>Controller: FArk Studio · Email: <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

LEGAL["de"]["privacy"] = {
    "title": "Datenschutzerklärung", "date": "8. Oktober 2026",
    "desc": "Welche Daten PosMetric verarbeitet, was auf Ihrem Handy bleibt und welche Rechte Sie haben.",
    "body": """
<div class="callout key"><p><strong>Grundsatz:</strong> Die Haltungsmessung läuft auf Ihrem Handy. Ihre Fotos, Messergebnisse und Trainingsdaten werden nicht an unsere Server gesendet.</p></div>
<div class="callout"><p><strong>Hinweis:</strong> PosMetric ist eine Fitness-App und kein Medizinprodukt.</p></div>

<h2>1. Daten, die auf Ihrem Handy bleiben</h2>
<p>Die folgenden Daten werden nur im Speicherbereich der App auf Ihrem Handy abgelegt und nicht an unsere Server gesendet:</p>
<ul>
<li><strong>Fotos:</strong> Fotos, die Sie für eine Messung aufnehmen oder aus der Galerie auswählen.</li>
<li><strong>Messergebnisse:</strong> Körperpunkte, Winkelberechnungen, Beobachtungen und frühere Messungen.</li>
<li><strong>Planeinstellungen:</strong> Ihr Ziel, empfindliche oder ruhende Bereiche, Erinnerungszeit und Coach-Auswahl.</li>
<li><strong>Trainingsdaten:</strong> Durchgeführte Übungen, aktive Tage, Serien, Abzeichen und der Fortschritt Ihres Plans.</li>
</ul>
<p><strong>Gerätesicherung:</strong> Ist die Sicherung Ihres Handys aktiviert (Google-Sicherung oder iCloud), kann das Betriebssystem diese Daten in eine Sicherung in Ihrem eigenen Konto übernehmen. Auf diese Sicherungen haben wir keinen Zugriff.</p>

<h2>2. Verarbeitete Daten</h2>
<h3>2.1. Kennung und Konto</h3>
<p>Beim ersten Start erhalten Sie über Firebase Authentication eine <strong>anonyme Nutzerkennung</strong>; Name oder E-Mail sind dafür nicht nötig. Wenn Sie sich mit Google oder Apple anmelden, werden <strong>E-Mail-Adresse</strong>, <strong>Anzeigename</strong> und <strong>Nutzerkennung</strong> zur Anmeldung verarbeitet und Ihre anonyme Kennung mit dieser Anmeldung verknüpft.</p>
<h3>2.2. Kostenloses Kontingent</h3>
<p>Um Missbrauch des kostenlosen Messkontingents zu verhindern, wird in Firebase Firestore nur Folgendes gespeichert:</p>
<ul>
<li>Die <strong>Anzahl der Messungen</strong> und der Zeitpunkt der letzten Messung, verknüpft mit Ihrer Nutzerkennung.</li>
<li>Ein <strong>anonymer Geräte-Hash</strong> (SHA-256), der Sie nicht identifiziert, und die Anzahl der Messungen auf diesem Gerät.</li>
</ul>
<p>Diese Einträge enthalten keine Fotos, Messergebnisse oder Trainingsdaten.</p>
<h3>2.3. Feedback</h3>
<p>Wenn Sie das Feedback-Formular in der App nutzen, werden Ihre Nachricht sowie App-Version und Geräteinformationen (Modell, Betriebssystem, Bildschirmauflösung) in Firestore gespeichert und an unsere Support-Adresse weitergeleitet.</p>
<h3>2.4. Abonnement</h3>
<p>PosMetric Pro wird über Google Play Billing gekauft (nach Veröffentlichung der iOS-Version auch über den App Store). Ihr Abostatus wird über RevenueCat geprüft; dazu erhält RevenueCat Ihre Nutzerkennung aus der App. Zahlungsdaten sehen wir nicht.</p>
<h3>2.5. Nutzungs-, Absturz- und Dienstdaten</h3>
<ul>
<li><strong>Firebase Analytics:</strong> Bildschirmaufrufe, Sitzungsdauer, allgemeine Geräteinformationen und anonyme Ereignisse (z. B. Messung abgeschlossen, Training gestartet oder beendet). Keine Fotos, Messergebnisse oder Angaben, die Sie direkt identifizieren.</li>
<li><strong>Werbe-ID:</strong> Firebase Analytics kann die Werbe-ID des Geräts ausschließlich für die Nutzungsanalyse verwenden. Die App zeigt keine Werbung.</li>
<li><strong>Firebase Crashlytics:</strong> Bei einem Absturz ein Fehlerbericht, Gerätemodell, Betriebssystem, App-Version und eine technische Kennung der Installation.</li>
<li><strong>Firebase App Check:</strong> Eine Integritätsprüfung, ob die App unverändert auf einem echten Gerät läuft.</li>
<li><strong>Firebase Remote Config und Storage:</strong> Aktualisierung von App-Einstellungen und Download der Coach-Sprachpakete. Dabei werden eine Installationskennung und Ihre IP-Adresse verarbeitet.</li>
</ul>

<h2>3. Berechtigungen</h2>
<ul>
<li><strong>Kamera:</strong> Nur für Messfotos.</li>
<li><strong>Fotos / Galerie:</strong> Damit Sie ein Foto für eine Messung auswählen können.</li>
<li><strong>Benachrichtigungen (optional):</strong> Für eine tägliche Erinnerung zur gewählten Uhrzeit. Erinnerungen werden auf Ihrem Handy geplant.</li>
</ul>

<h2>4. Weitergabe von Daten</h2>
<p>Wir verkaufen, vermieten oder teilen Ihre personenbezogenen Daten nicht zu Werbezwecken. Verarbeitet werden sie nur von diesen Dienstleistern, die wir für den Betrieb nutzen:</p>
<ul>
<li><strong>Google Firebase:</strong> Authentication, Firestore, Analytics, Crashlytics, App Check, Remote Config, Storage. <a href="https://policies.google.com/privacy">policies.google.com/privacy</a></li>
<li><strong>RevenueCat:</strong> Abo-Prüfung. <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a></li>
<li><strong>Google Play Billing und Apple App Store:</strong> Zahlungsabwicklung.</li>
<li><strong>Gesetzliche Pflichten:</strong> Soweit geltendes Recht es verlangt.</li>
</ul>
<p>Diese Dienstleister können Daten außerhalb der Türkei und des Europäischen Wirtschaftsraums verarbeiten, insbesondere in den USA.</p>

<h2>5. Datensicherheit</h2>
<ul>
<li>Daten auf dem Gerät liegen im geschützten App-Bereich (Sandbox) des Betriebssystems.</li>
<li>Alle an Server gesendeten Daten sind per TLS verschlüsselt.</li>
<li>Wir erheben nur die nötigsten Daten.</li>
<li>Beim Deinstallieren der App werden alle App-Daten auf dem Handy gelöscht.</li>
</ul>

<h2>6. Ihre Rechte und Löschung</h2>
<ul>
<li><strong>Konto und Daten löschen:</strong> In der App unter Profil &gt; Konto löschen entfernen Sie Ihr Konto und die zugehörigen Servereinträge. Ohne Zugang zur App folgen Sie den Schritten auf der <a href="/de/delete-account.html">Seite zur Kontolöschung</a>.</li>
<li><strong>Anonymer Geräte-Hash:</strong> Da er Sie nicht identifiziert, kann er nach der Kontolöschung zur Prüfung des kostenlosen Kontingents aufbewahrt werden.</li>
<li><strong>Weitere Rechte:</strong> Nach der DSGVO haben Sie das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht auf Beschwerde bei einer Aufsichtsbehörde. Schreiben Sie uns einfach.</li>
</ul>

<h2>7. Altersgrenze</h2>
<p>PosMetric richtet sich an Personen ab 18 Jahren. Wir erheben wissentlich keine Daten von Minderjährigen; erfahren wir davon, löschen wir sie.</p>

<h2>8. Änderungen</h2>
<p>Diese Erklärung kann gelegentlich aktualisiert werden. Die aktuelle Fassung steht immer auf dieser Seite.</p>

<h2>9. Kontakt</h2>
<p>Verantwortlich: FArk Studio · E-Mail: <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

LEGAL["es"]["privacy"] = {
    "title": "Política de privacidad", "date": "8 de octubre de 2026",
    "desc": "Qué datos trata PosMetric, cuáles se quedan en su móvil y cuáles son sus derechos.",
    "body": """
<div class="callout key"><p><strong>Principio básico:</strong> La medición de la postura se hace en su móvil. Sus fotos, resultados y datos de entrenamiento no se envían a nuestros servidores.</p></div>
<div class="callout"><p><strong>Nota:</strong> PosMetric es una app de fitness, no un dispositivo médico.</p></div>

<h2>1. Datos que se quedan en su móvil</h2>
<p>Los siguientes datos se guardan solo en el almacenamiento de la app en su móvil y no se envían a nuestros servidores:</p>
<ul>
<li><strong>Fotos:</strong> Las fotos que hace o elige de la galería para una medición.</li>
<li><strong>Resultados de medición:</strong> Puntos del cuerpo, cálculos de ángulos, observaciones y mediciones anteriores.</li>
<li><strong>Ajustes del plan:</strong> Su objetivo, zonas sensibles o en descanso, hora del recordatorio y coach elegido.</li>
<li><strong>Registros de entrenamiento:</strong> Movimientos realizados, días activos, rachas, insignias y el avance de su plan.</li>
</ul>
<p><strong>Copia de seguridad del dispositivo:</strong> Si la copia de seguridad del móvil está activada (Google o iCloud), el sistema operativo puede incluir estos datos en una copia en su propia cuenta. No tenemos acceso a esas copias.</p>

<h2>2. Datos que tratamos</h2>
<h3>2.1. Identificador y cuenta</h3>
<p>Al abrir la app por primera vez, Firebase Authentication le asigna un <strong>identificador de usuario anónimo</strong>; no se pide nombre ni correo. Si inicia sesión con Google o Apple, se tratan su <strong>correo electrónico</strong>, su <strong>nombre visible</strong> y su <strong>identificador de usuario</strong> para el inicio de sesión, y su identificador anónimo se vincula a esa cuenta.</p>
<h3>2.2. Uso gratuito</h3>
<p>Para evitar abusos del uso gratuito de mediciones, en Firebase Firestore solo se guarda:</p>
<ul>
<li>El <strong>número de mediciones</strong> y la hora de la última, vinculados a su identificador de usuario.</li>
<li>Un <strong>resumen anónimo del dispositivo</strong> (SHA-256) que no le identifica, y el número de mediciones en ese dispositivo.</li>
</ul>
<p>Estos registros no contienen fotos, resultados ni datos de entrenamiento.</p>
<h3>2.3. Comentarios</h3>
<p>Si usa el formulario de comentarios de la app, su mensaje junto con la versión de la app y datos del dispositivo (modelo, sistema operativo, resolución de pantalla) se guardan en Firestore y se reenvían a nuestro correo de soporte.</p>
<h3>2.4. Suscripción</h3>
<p>PosMetric Pro se compra a través de Google Play Billing (y del App Store cuando se publique la versión para iOS). El estado de su suscripción se verifica mediante RevenueCat, que recibe para ello su identificador de usuario de la app. Nunca vemos sus datos de pago.</p>
<h3>2.5. Datos de uso, errores y servicio</h3>
<ul>
<li><strong>Firebase Analytics:</strong> Pantallas vistas, duración de sesiones, información general del dispositivo y eventos anónimos (p. ej., completar una medición, empezar o terminar un entrenamiento). Sin fotos, resultados ni datos que le identifiquen directamente.</li>
<li><strong>ID de publicidad:</strong> Firebase Analytics puede usar el ID de publicidad del dispositivo solo para análisis de uso. La app no muestra anuncios.</li>
<li><strong>Firebase Crashlytics:</strong> Si la app falla, un informe de error, modelo del dispositivo, sistema operativo, versión de la app y un identificador técnico de la instalación.</li>
<li><strong>Firebase App Check:</strong> Una comprobación de integridad de que la app se ejecuta sin modificar en un dispositivo real.</li>
<li><strong>Firebase Remote Config y Storage:</strong> Actualizar los ajustes de la app y descargar los paquetes de voz del coach. Se tratan un identificador de instalación y su dirección IP.</li>
</ul>

<h2>3. Permisos</h2>
<ul>
<li><strong>Cámara:</strong> Solo para hacer las fotos de medición.</li>
<li><strong>Fotos / galería:</strong> Para que pueda elegir una foto para una medición.</li>
<li><strong>Notificaciones (opcional):</strong> Para un recordatorio diario a la hora que elija. Los recordatorios se programan en su móvil.</li>
</ul>

<h2>4. Cesión de datos</h2>
<p>No vendemos, alquilamos ni compartimos sus datos personales con fines de marketing. Solo los tratan estos proveedores que usamos para prestar el servicio:</p>
<ul>
<li><strong>Google Firebase:</strong> Authentication, Firestore, Analytics, Crashlytics, App Check, Remote Config, Storage. <a href="https://policies.google.com/privacy">policies.google.com/privacy</a></li>
<li><strong>RevenueCat:</strong> Verificación de suscripciones. <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a></li>
<li><strong>Google Play Billing y Apple App Store:</strong> Procesamiento de pagos.</li>
<li><strong>Obligaciones legales:</strong> Cuando lo exija la ley aplicable.</li>
</ul>
<p>Estos proveedores pueden tratar datos fuera de Turquía y del Espacio Económico Europeo, en particular en Estados Unidos.</p>

<h2>5. Seguridad</h2>
<ul>
<li>Los datos del dispositivo se guardan en el espacio protegido (sandbox) de la app.</li>
<li>Todos los datos enviados a servidores se cifran con TLS.</li>
<li>Solo recogemos los datos mínimos necesarios.</li>
<li>Al desinstalar la app se borran todos sus datos del móvil.</li>
</ul>

<h2>6. Sus derechos y eliminación</h2>
<ul>
<li><strong>Eliminar cuenta y datos:</strong> En la app, Perfil &gt; Eliminar cuenta borra su cuenta y sus registros en el servidor. Si no puede acceder a la app, siga los pasos de la <a href="/es/delete-account.html">página de eliminación de cuenta</a>.</li>
<li><strong>Resumen anónimo del dispositivo:</strong> Como no le identifica, puede conservarse tras eliminar la cuenta para controlar el uso gratuito.</li>
<li><strong>Otros derechos:</strong> Según el RGPD puede solicitar acceso, rectificación, supresión, limitación, portabilidad u oponerse al tratamiento, y presentar una reclamación ante una autoridad de control. Escríbanos.</li>
</ul>

<h2>7. Edad mínima</h2>
<p>PosMetric está pensada para mayores de 18 años. No recogemos a sabiendas datos de menores; si lo detectamos, los borramos.</p>

<h2>8. Cambios</h2>
<p>Esta política puede actualizarse. La versión vigente siempre se publica en esta página.</p>

<h2>9. Contacto</h2>
<p>Responsable: FArk Studio · Correo: <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

# --- Kullanım şartları

LEGAL["tr"]["terms"] = {
    "title": "Kullanım Şartları", "date": "8 Ekim 2026",
    "desc": "PosMetric'i kullanma koşulları, abonelik, deneme, iptal ve geri ödeme.",
    "body": """
<div class="callout warn"><p><strong>Önemli:</strong> PosMetric bir fitness uygulamasıdır; tıbbi cihaz değildir ve profesyonel sağlık hizmetinin yerine geçmez. Sağlığınızla ilgili sorularınız için bir sağlık profesyoneline danışın.</p></div>

<h2>1. Hizmetin tanımı</h2>
<p>PosMetric ("Uygulama"), FArk Studio ("Geliştirici") tarafından sunulan bir fitness ve hareket uygulamasıdır. Uygulama; kamerayla duruş ölçümü, kişisel antrenman planı, 3D koç rehberliği ve ilerleme takibi sunar.</p>

<h2>2. Kullanım koşulları</h2>
<ul>
<li>Uygulamayı kullanmak için 18 yaşından büyük olmanız gerekir.</li>
<li>Uygulamayı yalnızca kişisel ve ticari olmayan amaçlarla kullanabilirsiniz.</li>
<li>Kötüye kullanma, tersine mühendislik ve izinsiz erişim girişimleri yasaktır.</li>
<li>Uygulama içeriğini izinsiz kopyalamak, dağıtmak ya da değiştirmek yasaktır.</li>
</ul>

<h2>3. Sorumluluk reddi</h2>
<ul>
<li>Ölçüm sonuçları, hareket önerileri ve ilerleme raporları <strong>yalnızca bilgilendirme amaçlıdır</strong>; genel fitness ve farkındalık içindir.</li>
<li>Hareket sırasında rahatsızlık hissederseniz hareketi bırakın; gerekirse bir sağlık profesyoneline danışın.</li>
<li>Hareketleri kendi sorumluluğunuzda yaparsınız. Geliştirici, hareketler sırasında oluşabilecek yaralanmalardan sorumlu değildir.</li>
</ul>

<h2>4. Fikri mülkiyet</h2>
<p>Uygulama ve içeriği (tasarım, kod, 3D animasyonlar, sesler, algoritmalar, metinler) FArk Studio'nun fikri mülkiyetidir ve telif hakkıyla korunur. Üçüncü taraf bileşenler kendi lisanslarına tabidir (bkz. <a href="/developer.html">Hakkımızda</a>).</p>

<h2>5. Abonelik ve ücretlendirme</h2>
<h3>5.1. Ücretsiz sürüm ve PosMetric Pro</h3>
<p>PosMetric'in ücretsiz sürümü süresizdir. Hangi özelliklerin ücretsiz, hangilerinin <strong>PosMetric Pro</strong> kapsamında olduğu uygulamadaki abonelik sayfasında gösterilir.</p>
<h3>5.2. Planlar ve fiyatlar</h3>
<p>Abonelik süreleri ve güncel fiyatlar satın almadan önce uygulamadaki abonelik sayfasında gösterilir. Fiyatlar ülkeye ve para birimine göre değişebilir.</p>
<h3>5.3. Ücretsiz deneme</h3>
<p>Ücretsiz deneme sunulduğunda, deneme süresi bitmeden iptal etmezseniz abonelik başlar ve ücret alınır. Deneme süresi ve sonrasında alınacak ücret onayınızdan önce gösterilir.</p>
<h3>5.4. Otomatik yenileme</h3>
<ul>
<li>Abonelikler <strong>otomatik olarak yenilenir</strong>; dönem bitiminden en az 24 saat önce iptal edilmezse aynı süre için yenilenir.</li>
<li>Yenileme ücreti dönemin bitiminden önceki 24 saat içinde tahsil edilir.</li>
</ul>
<h3>5.5. İptal</h3>
<ul>
<li>Aboneliğinizi istediğiniz zaman iptal edebilirsiniz.</li>
<li><strong>Android (Google Play):</strong> Google Play Store → profil simgesi → Ödemeler ve abonelikler → Abonelikler → PosMetric → İptal et.</li>
<li><strong>iOS (App Store, yayımlandığında):</strong> Ayarlar → adınız → Abonelikler → PosMetric → Aboneliği İptal Et.</li>
<li>İptalden sonra dönem sonuna kadar Pro özelliklerini kullanmaya devam edersiniz. Hesabınızı silmek aboneliği iptal etmez.</li>
</ul>
<h3>5.6. Geri ödeme</h3>
<p>Geri ödeme talepleri satın almanın yapıldığı mağazanın politikasına tabidir: <a href="https://support.google.com/googleplay/answer/2479637">Google Play</a> · <a href="https://support.apple.com/118223">Apple</a>.</p>

<h2>6. Sorumluluğun sınırlandırılması</h2>
<p>Uygulama "olduğu gibi" sunulur. Geliştirici; ölçüm sonuçlarının doğruluğunu ya da eksiksizliğini, uygulamanın kesintisiz ya da hatasız çalışacağını garanti etmez ve yürürlükteki hukukun izin verdiği ölçüde, kullanımdan doğan doğrudan ya da dolaylı zararlardan sorumlu değildir.</p>

<h2>7. Değişiklikler</h2>
<p>Bu şartlar güncellenebilir; güncel sürüm bu sayfada yayımlanır. Uygulamayı kullanmaya devam etmeniz güncel şartları kabul ettiğiniz anlamına gelir.</p>

<h2>8. Uygulanacak hukuk</h2>
<p>Bu şartlar Türkiye Cumhuriyeti yasalarına tabidir. Bulunduğunuz ülkenin tüketiciyi koruyan zorunlu kuralları saklıdır.</p>

<h2>9. İletişim</h2>
<p>FArk Studio · <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

LEGAL["en"]["terms"] = {
    "title": "Terms of Use", "date": "October 8, 2026",
    "desc": "Terms for using PosMetric: subscriptions, free trials, cancellation and refunds.",
    "body": """
<div class="callout warn"><p><strong>Important:</strong> PosMetric is a fitness app; it is not a medical device and does not replace professional health care. For questions about your health, consult a health professional.</p></div>

<h2>1. The service</h2>
<p>PosMetric (the "App") is a fitness and movement app provided by FArk Studio (the "Developer"). It offers camera-based posture measurement, a personal workout plan, 3D coach guidance and progress tracking.</p>

<h2>2. Conditions of use</h2>
<ul>
<li>You must be over 18 to use the App.</li>
<li>You may use the App only for personal, non-commercial purposes.</li>
<li>Misuse, reverse engineering and unauthorized access attempts are prohibited.</li>
<li>Copying, distributing or modifying App content without permission is prohibited.</li>
</ul>

<h2>3. Disclaimer</h2>
<ul>
<li>Measurement results, movement suggestions and progress reports are <strong>for information only</strong>, for general fitness and awareness.</li>
<li>If you feel discomfort during a movement, stop; consult a health professional if needed.</li>
<li>You perform movements on your own responsibility. The Developer is not responsible for injuries that may occur during them.</li>
</ul>

<h2>4. Intellectual property</h2>
<p>The App and its content (design, code, 3D animations, voices, algorithms, texts) are the intellectual property of FArk Studio and protected by copyright. Third-party components are subject to their own licenses (see <a href="/en/developer.html">About us</a>).</p>

<h2>5. Subscriptions and billing</h2>
<h3>5.1. Free version and PosMetric Pro</h3>
<p>The free version of PosMetric has no time limit. Which features are free and which are part of <strong>PosMetric Pro</strong> is shown on the subscription page in the App.</p>
<h3>5.2. Plans and prices</h3>
<p>Subscription periods and current prices are shown on the subscription page in the App before you buy. Prices may vary by country and currency.</p>
<h3>5.3. Free trial</h3>
<p>Where a free trial is offered, the subscription starts and you are charged unless you cancel before the trial ends. The trial length and the price charged afterwards are shown before you confirm.</p>
<h3>5.4. Auto-renewal</h3>
<ul>
<li>Subscriptions <strong>renew automatically</strong> for the same period unless cancelled at least 24 hours before the end of the current period.</li>
<li>Renewal is charged within the 24 hours before the period ends.</li>
</ul>
<h3>5.5. Cancellation</h3>
<ul>
<li>You can cancel at any time.</li>
<li><strong>Android (Google Play):</strong> Google Play Store → profile icon → Payments &amp; subscriptions → Subscriptions → PosMetric → Cancel.</li>
<li><strong>iOS (App Store, once released):</strong> Settings → your name → Subscriptions → PosMetric → Cancel Subscription.</li>
<li>After cancelling you keep Pro features until the end of the period. Deleting your account does not cancel your subscription.</li>
</ul>
<h3>5.6. Refunds</h3>
<p>Refunds follow the policy of the store you bought from: <a href="https://support.google.com/googleplay/answer/2479637">Google Play</a> · <a href="https://support.apple.com/118223">Apple</a>.</p>

<h2>6. Limitation of liability</h2>
<p>The App is provided "as is". The Developer does not guarantee that measurement results are accurate or complete, or that the App will run without interruption or errors, and, to the extent permitted by applicable law, is not liable for direct or indirect damages arising from its use.</p>

<h2>7. Changes</h2>
<p>These terms may be updated; the current version is published on this page. Continuing to use the App means you accept the current terms.</p>

<h2>8. Governing law</h2>
<p>These terms are governed by the laws of the Republic of Türkiye. Mandatory consumer protection rules of your country of residence remain unaffected.</p>

<h2>9. Contact</h2>
<p>FArk Studio · <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

LEGAL["de"]["terms"] = {
    "title": "Nutzungsbedingungen", "date": "8. Oktober 2026",
    "desc": "Bedingungen für die Nutzung von PosMetric: Abos, Testzeitraum, Kündigung und Erstattung.",
    "body": """
<div class="callout warn"><p><strong>Wichtig:</strong> PosMetric ist eine Fitness-App; sie ist kein Medizinprodukt und ersetzt keine professionelle Gesundheitsversorgung. Wenden Sie sich bei Fragen zu Ihrer Gesundheit an eine Fachperson.</p></div>

<h2>1. Leistungsbeschreibung</h2>
<p>PosMetric (die „App") ist eine Fitness- und Bewegungs-App von FArk Studio (der „Entwickler"). Sie bietet eine kamerabasierte Haltungsmessung, einen persönlichen Trainingsplan, Anleitung durch einen 3D-Coach und eine Fortschrittsübersicht.</p>

<h2>2. Nutzungsvoraussetzungen</h2>
<ul>
<li>Für die Nutzung müssen Sie mindestens 18 Jahre alt sein.</li>
<li>Die App darf nur für private, nicht kommerzielle Zwecke genutzt werden.</li>
<li>Missbrauch, Reverse Engineering und unbefugte Zugriffsversuche sind untersagt.</li>
<li>Inhalte der App dürfen ohne Erlaubnis nicht kopiert, verbreitet oder verändert werden.</li>
</ul>

<h2>3. Haftungshinweis</h2>
<ul>
<li>Messergebnisse, Übungsvorschläge und Fortschrittsberichte dienen <strong>nur der Information</strong>, für allgemeine Fitness und Achtsamkeit.</li>
<li>Wenn Sie sich bei einer Übung unwohl fühlen, brechen Sie sie ab und wenden Sie sich bei Bedarf an eine Fachperson.</li>
<li>Sie führen die Übungen auf eigene Verantwortung aus.</li>
</ul>

<h2>4. Geistiges Eigentum</h2>
<p>Die App und ihre Inhalte (Design, Code, 3D-Animationen, Stimmen, Algorithmen, Texte) sind geistiges Eigentum von FArk Studio und urheberrechtlich geschützt. Komponenten Dritter unterliegen ihren eigenen Lizenzen (siehe <a href="/de/developer.html">Über uns</a>).</p>

<h2>5. Abonnement und Zahlung</h2>
<h3>5.1. Kostenlose Version und PosMetric Pro</h3>
<p>Die kostenlose Version von PosMetric ist unbefristet. Welche Funktionen kostenlos sind und welche zu <strong>PosMetric Pro</strong> gehören, sehen Sie auf der Abo-Seite in der App.</p>
<h3>5.2. Laufzeiten und Preise</h3>
<p>Laufzeiten und aktuelle Preise werden vor dem Kauf auf der Abo-Seite der App angezeigt. Preise können je nach Land und Währung variieren.</p>
<h3>5.3. Kostenloser Testzeitraum</h3>
<p>Wird ein kostenloser Testzeitraum angeboten, beginnt das Abo kostenpflichtig, wenn Sie nicht vor dessen Ende kündigen. Dauer und anschließender Preis werden vor Ihrer Bestätigung angezeigt.</p>
<h3>5.4. Automatische Verlängerung</h3>
<ul>
<li>Abos <strong>verlängern sich automatisch</strong> um die gleiche Laufzeit, wenn sie nicht spätestens 24 Stunden vor Ablauf gekündigt werden.</li>
<li>Die Verlängerung wird innerhalb der letzten 24 Stunden der Laufzeit berechnet.</li>
</ul>
<h3>5.5. Kündigung</h3>
<ul>
<li>Sie können jederzeit kündigen.</li>
<li><strong>Android (Google Play):</strong> Google Play Store → Profilsymbol → Zahlungen und Abos → Abos → PosMetric → Kündigen.</li>
<li><strong>iOS (App Store, nach Veröffentlichung):</strong> Einstellungen → Ihr Name → Abonnements → PosMetric → Abonnement kündigen.</li>
<li>Nach der Kündigung nutzen Sie Pro bis zum Ende der Laufzeit weiter. Das Löschen Ihres Kontos kündigt das Abo nicht.</li>
</ul>
<h3>5.6. Erstattung</h3>
<p>Erstattungen richten sich nach den Regeln des Stores, in dem Sie gekauft haben: <a href="https://support.google.com/googleplay/answer/2479637">Google Play</a> · <a href="https://support.apple.com/118223">Apple</a>. Ihre gesetzlichen Rechte bleiben unberührt.</p>

<h2>6. Haftungsbeschränkung</h2>
<p>Die App wird ohne Gewähr bereitgestellt. Der Entwickler garantiert nicht, dass Messergebnisse genau oder vollständig sind oder dass die App unterbrechungs- und fehlerfrei läuft. Die Haftung ist im gesetzlich zulässigen Umfang beschränkt; die Haftung für Vorsatz, grobe Fahrlässigkeit sowie für Schäden an Leben, Körper und Gesundheit bleibt unberührt.</p>

<h2>7. Änderungen</h2>
<p>Diese Bedingungen können aktualisiert werden; die aktuelle Fassung steht auf dieser Seite.</p>

<h2>8. Anwendbares Recht</h2>
<p>Es gilt das Recht der Republik Türkei. Zwingende Verbraucherschutzvorschriften Ihres Wohnsitzlandes bleiben unberührt.</p>

<h2>9. Kontakt</h2>
<p>FArk Studio · <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

LEGAL["es"]["terms"] = {
    "title": "Términos de uso", "date": "8 de octubre de 2026",
    "desc": "Condiciones de uso de PosMetric: suscripciones, prueba gratuita, cancelación y reembolsos.",
    "body": """
<div class="callout warn"><p><strong>Importante:</strong> PosMetric es una app de fitness; no es un dispositivo médico y no sustituye la atención sanitaria profesional. Para dudas sobre su salud, consulte a un profesional sanitario.</p></div>

<h2>1. El servicio</h2>
<p>PosMetric (la "App") es una app de fitness y movimiento ofrecida por FArk Studio (el "Desarrollador"). Ofrece medición de la postura con la cámara, un plan de entrenamiento personal, guía de un coach en 3D y seguimiento del progreso.</p>

<h2>2. Condiciones de uso</h2>
<ul>
<li>Debe ser mayor de 18 años para usar la App.</li>
<li>Solo puede usarla con fines personales y no comerciales.</li>
<li>Se prohíbe el uso indebido, la ingeniería inversa y los intentos de acceso no autorizado.</li>
<li>Se prohíbe copiar, distribuir o modificar el contenido de la App sin permiso.</li>
</ul>

<h2>3. Aviso</h2>
<ul>
<li>Los resultados de medición, las sugerencias de movimientos y los informes de progreso son <strong>solo informativos</strong>, para el fitness y la conciencia corporal en general.</li>
<li>Si nota molestias durante un movimiento, deténgase y, si es necesario, consulte a un profesional sanitario.</li>
<li>Realiza los movimientos bajo su propia responsabilidad. El Desarrollador no es responsable de lesiones que puedan producirse durante ellos.</li>
</ul>

<h2>4. Propiedad intelectual</h2>
<p>La App y su contenido (diseño, código, animaciones 3D, voces, algoritmos, textos) son propiedad intelectual de FArk Studio y están protegidos por derechos de autor. Los componentes de terceros se rigen por sus propias licencias (ver <a href="/es/developer.html">Sobre nosotros</a>).</p>

<h2>5. Suscripción y pagos</h2>
<h3>5.1. Versión gratuita y PosMetric Pro</h3>
<p>La versión gratuita de PosMetric no caduca. Qué funciones son gratuitas y cuáles forman parte de <strong>PosMetric Pro</strong> se muestra en la página de suscripción de la App.</p>
<h3>5.2. Planes y precios</h3>
<p>Los periodos y precios vigentes se muestran en la página de suscripción antes de comprar. Pueden variar según el país y la moneda.</p>
<h3>5.3. Prueba gratuita</h3>
<p>Cuando se ofrece una prueba gratuita, la suscripción empieza y se cobra si no cancela antes de que termine. La duración de la prueba y el precio posterior se muestran antes de confirmar.</p>
<h3>5.4. Renovación automática</h3>
<ul>
<li>Las suscripciones <strong>se renuevan automáticamente</strong> por el mismo periodo si no se cancelan al menos 24 horas antes de que termine.</li>
<li>La renovación se cobra dentro de las 24 horas previas al fin del periodo.</li>
</ul>
<h3>5.5. Cancelación</h3>
<ul>
<li>Puede cancelar en cualquier momento.</li>
<li><strong>Android (Google Play):</strong> Google Play Store → icono de perfil → Pagos y suscripciones → Suscripciones → PosMetric → Cancelar.</li>
<li><strong>iOS (App Store, cuando se publique):</strong> Ajustes → su nombre → Suscripciones → PosMetric → Cancelar suscripción.</li>
<li>Tras cancelar, conserva Pro hasta el final del periodo. Eliminar su cuenta no cancela la suscripción.</li>
</ul>
<h3>5.6. Reembolsos</h3>
<p>Los reembolsos siguen la política de la tienda donde compró: <a href="https://support.google.com/googleplay/answer/2479637">Google Play</a> · <a href="https://support.apple.com/118223">Apple</a>.</p>

<h2>6. Limitación de responsabilidad</h2>
<p>La App se ofrece "tal cual". El Desarrollador no garantiza que los resultados sean exactos o completos ni que la App funcione sin interrupciones ni errores y, en la medida permitida por la ley aplicable, no responde de daños directos o indirectos derivados de su uso.</p>

<h2>7. Cambios</h2>
<p>Estos términos pueden actualizarse; la versión vigente se publica en esta página.</p>

<h2>8. Ley aplicable</h2>
<p>Estos términos se rigen por las leyes de la República de Turquía, sin perjuicio de las normas imperativas de protección del consumidor de su país de residencia.</p>

<h2>9. Contacto</h2>
<p>FArk Studio · <a href="mailto:info@physiometric.app">info@physiometric.app</a></p>
""",
}

# --- Hesap silme

def _delete(lang, t):
    rows = "".join(f"<tr><td><strong>{a}</strong><small>{b}</small></td><td>{c}</td></tr>" for a, b, c in t["rows"])
    steps = "".join(f"<li>{s}</li>" for s in t["app_steps"])
    mail = "".join(f"<li>{s}</li>" for s in t["mail_steps"])
    return {
        "title": t["title"], "date": t["date"], "desc": t["desc"],
        "body": f"""
<div class="callout warn"><p>{t['warn']}</p></div>
<h2>{t['m1']}</h2><ol>{steps}</ol>
<h2>{t['m2']}</h2><ol>{mail}</ol>
<p>{t['sla']}</p>
<h2>{t['what']}</h2>
<table class="table"><thead><tr><th>{t['th'][0]}</th><th>{t['th'][1]}</th></tr></thead><tbody>{rows}</tbody></table>
<div class="callout"><p>{t['sub']}</p></div>
<p>{t['more']}</p>
""",
    }

LEGAL["tr"]["delete-account"] = _delete("tr", {
    "title": "Hesap Silme", "date": "8 Ekim 2026",
    "desc": "PosMetric hesabınızı uygulamadan ya da e-postayla nasıl silersiniz ve hangi veriler silinir.",
    "warn": "<strong>Önemli:</strong> Hesap silme <strong>geri alınamaz</strong>. Hesabınıza bağlı sunucu kayıtları kalıcı olarak silinir.",
    "m1": "Yöntem 1: Uygulamadan silme (önerilen)",
    "app_steps": ["PosMetric uygulamasını açın.", "<strong>Profil</strong> sekmesine gidin.", "<strong>Hesabı Sil</strong>'e dokunun ve onaylayın."],
    "m2": "Yöntem 2: E-postayla silme talebi",
    "mail_steps": ["Giriş yaptığınız e-posta adresinden yazın.", 'Adres: <a href="mailto:info@physiometric.app?subject=Hesap%20Silme%20Talebi%20-%20PosMetric">info@physiometric.app</a>', 'Konu: "Hesap Silme Talebi - PosMetric"'],
    "sla": "Talebiniz doğrulandıktan sonra verileriniz en geç 48 saat içinde silinir.",
    "what": "Hesap silinince ne olur?",
    "th": ["Veri", "Ne olur"],
    "rows": [
        ("Oturum bilgileri", "Firebase Authentication", "Talep işlendiği anda kalıcı olarak silinir."),
        ("Ücretsiz kullanım sayacı", "Kimliğinize bağlı kayıt", "Silinir. Kişiyi tanımlamayan anonim cihaz özeti ücretsiz hak kontrolü için saklanabilir."),
        ("Ölçüm ve antrenman verileri", "Fotoğraflar, sonuçlar, kayıtlar", "Sunucularımızda zaten tutulmaz. Telefonunuzda kalır; uygulamayı kaldırdığınızda tamamen silinir."),
        ("Hata kayıtları", "Firebase Crashlytics", "Teknik çökme kayıtları en geç 90 gün içinde kendiliğinden silinir."),
    ],
    "sub": "<strong>Abonelik:</strong> Hesabı silmek aboneliği iptal etmez. Aboneliğinizi Google Play'den (iOS'ta App Store'dan) iptal edin.",
    "more": 'Ayrıntılar için <a href="/privacy.html">Gizlilik Politikası</a>.',
})
LEGAL["en"]["delete-account"] = _delete("en", {
    "title": "Delete Account", "date": "October 8, 2026",
    "desc": "How to delete your PosMetric account in the app or by email, and what gets deleted.",
    "warn": "<strong>Important:</strong> Deleting your account <strong>cannot be undone</strong>. Server records linked to your account are permanently deleted.",
    "m1": "Option 1: Delete in the app (recommended)",
    "app_steps": ["Open the PosMetric app.", "Go to the <strong>Profile</strong> tab.", "Tap <strong>Delete Account</strong> and confirm."],
    "m2": "Option 2: Request deletion by email",
    "mail_steps": ["Write from the email address you signed in with.", 'Address: <a href="mailto:info@physiometric.app?subject=Account%20Deletion%20Request%20-%20PosMetric">info@physiometric.app</a>', 'Subject: "Account Deletion Request - PosMetric"'],
    "sla": "Once your request is verified, your data is deleted within 48 hours.",
    "what": "What happens when you delete your account?",
    "th": ["Data", "What happens"],
    "rows": [
        ("Sign-in data", "Firebase Authentication", "Permanently deleted as soon as the request is processed."),
        ("Free allowance counter", "Record linked to your ID", "Deleted. An anonymous device hash that does not identify you may be kept to enforce the free allowance."),
        ("Measurement and workout data", "Photos, results, records", "Never stored on our servers. It stays on your phone and is fully deleted when you uninstall the app."),
        ("Crash logs", "Firebase Crashlytics", "Technical crash records are deleted automatically within 90 days."),
    ],
    "sub": "<strong>Subscription:</strong> Deleting your account does not cancel your subscription. Cancel it in Google Play (or the App Store on iOS).",
    "more": 'More details in our <a href="/en/privacy.html">Privacy Policy</a>.',
})
LEGAL["de"]["delete-account"] = _delete("de", {
    "title": "Konto löschen", "date": "8. Oktober 2026",
    "desc": "So löschen Sie Ihr PosMetric-Konto in der App oder per E-Mail, und welche Daten gelöscht werden.",
    "warn": "<strong>Wichtig:</strong> Die Kontolöschung <strong>kann nicht rückgängig gemacht werden</strong>. Mit Ihrem Konto verknüpfte Servereinträge werden dauerhaft gelöscht.",
    "m1": "Weg 1: In der App löschen (empfohlen)",
    "app_steps": ["Öffnen Sie die PosMetric-App.", "Gehen Sie zum Tab <strong>Profil</strong>.", "Tippen Sie auf <strong>Konto löschen</strong> und bestätigen Sie."],
    "m2": "Weg 2: Löschung per E-Mail anfordern",
    "mail_steps": ["Schreiben Sie von der E-Mail-Adresse, mit der Sie angemeldet sind.", 'Adresse: <a href="mailto:info@physiometric.app?subject=Antrag%20auf%20Kontol%C3%B6schung%20-%20PosMetric">info@physiometric.app</a>', 'Betreff: „Antrag auf Kontolöschung - PosMetric"'],
    "sla": "Nach Prüfung Ihres Antrags werden Ihre Daten innerhalb von 48 Stunden gelöscht.",
    "what": "Was passiert beim Löschen?",
    "th": ["Daten", "Was passiert"],
    "rows": [
        ("Anmeldedaten", "Firebase Authentication", "Werden mit Bearbeitung des Antrags dauerhaft gelöscht."),
        ("Zähler für das kostenlose Kontingent", "Eintrag zu Ihrer Kennung", "Wird gelöscht. Ein anonymer Geräte-Hash, der Sie nicht identifiziert, kann zur Prüfung des Kontingents aufbewahrt werden."),
        ("Mess- und Trainingsdaten", "Fotos, Ergebnisse, Einträge", "Liegen nie auf unseren Servern. Sie bleiben auf Ihrem Handy und werden beim Deinstallieren vollständig gelöscht."),
        ("Absturzprotokolle", "Firebase Crashlytics", "Technische Absturzdaten werden nach spätestens 90 Tagen automatisch gelöscht."),
    ],
    "sub": "<strong>Abonnement:</strong> Das Löschen des Kontos kündigt Ihr Abo nicht. Kündigen Sie es bei Google Play (unter iOS im App Store).",
    "more": 'Mehr in unserer <a href="/de/privacy.html">Datenschutzerklärung</a>.',
})
LEGAL["es"]["delete-account"] = _delete("es", {
    "title": "Eliminar cuenta", "date": "8 de octubre de 2026",
    "desc": "Cómo eliminar su cuenta de PosMetric desde la app o por correo, y qué datos se borran.",
    "warn": "<strong>Importante:</strong> Eliminar la cuenta <strong>no se puede deshacer</strong>. Los registros del servidor vinculados a su cuenta se borran de forma permanente.",
    "m1": "Opción 1: Eliminar desde la app (recomendado)",
    "app_steps": ["Abra la app PosMetric.", "Vaya a la pestaña <strong>Perfil</strong>.", "Toque <strong>Eliminar cuenta</strong> y confirme."],
    "m2": "Opción 2: Solicitar la eliminación por correo",
    "mail_steps": ["Escriba desde el correo con el que inició sesión.", 'Dirección: <a href="mailto:info@physiometric.app?subject=Solicitud%20de%20eliminaci%C3%B3n%20de%20cuenta%20-%20PosMetric">info@physiometric.app</a>', 'Asunto: "Solicitud de eliminación de cuenta - PosMetric"'],
    "sla": "Una vez verificada la solicitud, sus datos se borran en un plazo de 48 horas.",
    "what": "¿Qué pasa al eliminar la cuenta?",
    "th": ["Datos", "Qué pasa"],
    "rows": [
        ("Datos de inicio de sesión", "Firebase Authentication", "Se borran de forma permanente al procesar la solicitud."),
        ("Contador de uso gratuito", "Registro vinculado a su identificador", "Se borra. Puede conservarse un resumen anónimo del dispositivo, que no le identifica, para controlar el uso gratuito."),
        ("Datos de medición y entrenamiento", "Fotos, resultados, registros", "Nunca se guardan en nuestros servidores. Se quedan en su móvil y se borran por completo al desinstalar la app."),
        ("Registros de errores", "Firebase Crashlytics", "Los registros técnicos de fallos se borran automáticamente en un máximo de 90 días."),
    ],
    "sub": "<strong>Suscripción:</strong> Eliminar la cuenta no cancela la suscripción. Cancélela en Google Play (en iOS, en el App Store).",
    "more": 'Más detalles en nuestra <a href="/es/privacy.html">Política de privacidad</a>.',
})

# --- Hakkımızda

def _about(t):
    return {
        "title": t["title"], "date": None, "desc": t["desc"],
        "body": f"""
<p style="font-size:19px">{t['intro']}</p>
<h2>{t['contact_h']}</h2>
<div class="contact">
  <div class="card"><b>{t['labels'][0]}</b><a href="mailto:info@physiometric.app">info@physiometric.app</a></div>
  <div class="card"><b>{t['labels'][1]}</b>{t['country']}</div>
  <div class="card"><b>{t['labels'][2]}</b><a href="https://physiometric.app">physiometric.app</a></div>
</div>
<h2>{t['apps_h']}</h2>
<div class="card" style="display:flex;gap:16px;align-items:center"><img src="/assets/app_icon.png" alt="" width="56" height="56" style="border-radius:14px"><div><strong>PosMetric</strong><p>{t['app_desc']}</p></div></div>
<h2>{t['credits_h']}</h2>
<ul>
<li>{t['credits'][0]} — Microsoft Rocketbox, MIT, © 2020 Microsoft. <a href="https://github.com/microsoft/Microsoft-Rocketbox">github.com/microsoft/Microsoft-Rocketbox</a></li>
<li>three.js — MIT, © 2010–2024 three.js authors. <a href="https://threejs.org">threejs.org</a></li>
<li>{t['credits'][1]} — Inter, SIL Open Font License 1.1, © The Inter Project Authors.</li>
</ul>
<h2>{t['legal_h']}</h2>
<p>{t['legal']}</p>
""",
    }

LEGAL["tr"]["developer"] = _about({
    "title": "Hakkımızda", "desc": "PosMetric'i geliştiren bağımsız stüdyo FArk Studio ve iletişim bilgileri.",
    "intro": "<strong>FArk Studio</strong> Türkiye'de bağımsız bir geliştirici stüdyosudur. PosMetric'i, uzun saatler oturan herkesin kısa ve düzenli hareketlerle günlük bir alışkanlık kazanabilmesi için geliştiriyoruz.",
    "contact_h": "İletişim", "labels": ["E-posta", "Konum", "Web sitesi"], "country": "Türkiye",
    "apps_h": "Uygulamalarımız",
    "app_desc": "Telefon kamerasıyla duruş ölçümü, kişisel antrenman planı ve 3D koç. Android'de; iOS yakında.",
    "credits_h": "Teşekkürler ve lisanslar", "credits": ["3D koç karakterleri", "Yazı tipi"],
    "legal_h": "Yasal", "legal": '<a href="/privacy.html">Gizlilik Politikası</a> · <a href="/terms.html">Kullanım Şartları</a> · <a href="/delete-account.html">Hesap Silme</a>',
})
LEGAL["en"]["developer"] = _about({
    "title": "About us", "desc": "FArk Studio, the independent studio behind PosMetric, and how to reach us.",
    "intro": "<strong>FArk Studio</strong> is an independent developer studio based in Türkiye. We build PosMetric so that anyone who sits for long hours can build a daily habit of short, regular movement.",
    "contact_h": "Contact", "labels": ["Email", "Location", "Website"], "country": "Türkiye",
    "apps_h": "Our apps",
    "app_desc": "Posture measurement with your phone camera, a personal workout plan and a 3D coach. On Android; iOS coming soon.",
    "credits_h": "Credits and licenses", "credits": ["3D coach characters", "Typeface"],
    "legal_h": "Legal", "legal": '<a href="/en/privacy.html">Privacy Policy</a> · <a href="/en/terms.html">Terms of Use</a> · <a href="/en/delete-account.html">Delete Account</a>',
})
LEGAL["de"]["developer"] = _about({
    "title": "Über uns", "desc": "FArk Studio, das unabhängige Studio hinter PosMetric, und unsere Kontaktdaten.",
    "intro": "<strong>FArk Studio</strong> ist ein unabhängiges Entwicklerstudio aus der Türkei. Wir entwickeln PosMetric, damit alle, die viel sitzen, mit kurzen, regelmäßigen Übungen eine tägliche Gewohnheit aufbauen können.",
    "contact_h": "Kontakt", "labels": ["E-Mail", "Standort", "Website"], "country": "Türkei",
    "apps_h": "Unsere Apps",
    "app_desc": "Haltungsmessung mit der Handykamera, persönlicher Trainingsplan und 3D-Coach. Für Android; iOS folgt.",
    "credits_h": "Danksagungen und Lizenzen", "credits": ["3D-Coach-Figuren", "Schrift"],
    "legal_h": "Rechtliches", "legal": '<a href="/de/privacy.html">Datenschutz</a> · <a href="/de/terms.html">Nutzungsbedingungen</a> · <a href="/de/delete-account.html">Konto löschen</a>',
})
LEGAL["es"]["developer"] = _about({
    "title": "Sobre nosotros", "desc": "FArk Studio, el estudio independiente detrás de PosMetric, y cómo contactarnos.",
    "intro": "<strong>FArk Studio</strong> es un estudio de desarrollo independiente con sede en Turquía. Creamos PosMetric para que cualquier persona que pase muchas horas sentada pueda crear un hábito diario de movimiento corto y regular.",
    "contact_h": "Contacto", "labels": ["Correo", "Ubicación", "Sitio web"], "country": "Turquía",
    "apps_h": "Nuestras apps",
    "app_desc": "Medición de la postura con la cámara del móvil, plan de entrenamiento personal y coach en 3D. En Android; iOS próximamente.",
    "credits_h": "Créditos y licencias", "credits": ["Personajes 3D del coach", "Tipografía"],
    "legal_h": "Legal", "legal": '<a href="/es/privacy.html">Política de privacidad</a> · <a href="/es/terms.html">Términos de uso</a> · <a href="/es/delete-account.html">Eliminar cuenta</a>',
})



# Mini kontrol (/mini-check.html): uygulamadaki ön çekimin tarayıcıdaki demosu. Yönlendirme
# (live_*), sonuç ekranı (pivot_result_*), alan adları (diagnosis*) ve gözlem cümleleri
# (individual*) uygulamanın ARB metinleriyle aynıdır; uygulamada değişirse burası da güncellenir.
# Sonuç ücretsiz sürümdeki gibidir: alanın adı ve gözlem cümlesi açık, ayrıntı Pro.
CHECK = {
    "tr": {
        "title": "Mini kontrol — PosMetric",
        "desc": "Kameranın karşısında dur; koçun seni sesle yönlendirsin, ölçüm kendiliğinden yapılsın. Görüntü cihazından çıkmaz.",
        "eyebrow": "Tarayıcıda dene",
        "h1": "Mini kontrol",
        "lead": "Uygulamadaki ön çekimin küçük bir denemesi. Koçun seni sesle yönlendirir; doğru durduğunda ölçüm kendiliğinden yapılır.",
        "privacy": "Görüntü cihazından çıkmaz. Ölçüm tarayıcında yapılır; hiçbir yere gönderilmez, kaydedilmez.",
        "pick": "Koçunu seç",
        "sound": "Sesli yönlendirme",
        "tips_title": "Nasıl durmalısın?",
        "tips": [
            "Bilgisayarı ya da telefonu bel hizasında bir yere koy.",
            "Birkaç adım geri çekil; başından ayak bileklerine kadar görünmelisin.",
            "Kameraya önden bak, kolların yanında serbest dursun.",
            "Işık önünden gelsin, arkanda pencere olmasın.",
        ],
        "start": "Kontrole başla",
        "again": "Tekrar ölç",
        "loading": "Hazırlanıyor…",
        "cam_error": "Kamera açılamadı. Tarayıcının kamera iznini kontrol et ya da tam kontrolü uygulamada yap.",
        "unsupported": "Bu tarayıcı mini kontrolü çalıştıramıyor. Tam kontrolü uygulamada yapabilirsin.",
        "app_title": "Uygulamada seni neler bekliyor?",
        "app_lead": "Bu ölçüm uygulamadaki sistemin aynısıyla yapıldı. Uygulamada daha fazlası var:",
        "free_tag": "Ücretsiz",
        "app_items": [
            ("📐", "Tam kontrol", "Önden ve yandan iki fotoğrafla 23 alana bakılır; burada yalnızca 2'sini gördün.", False),
            ("🎯", "Sana göre plan", "Ölçümünde öne çıkan alanlara öncelik veren 3 hareketlik bir plan.", True),
            ("🗣️", "Koçun yanında", "{fem} ya da {mal} her hareketi seninle birlikte yapar, sesle sayar.", False),
            ("☕", "Masa başı molası", "Oturduğun yerde 3 kısa hareket.", True),
            ("🔥", "Halkalar ve seri", "Hareket ettiğin her gün halkaların dolar.", True),
        ],
        "cta_title": "Tam kontrol ve planın uygulamada",
        "live": {
            "moving": "Sabit durun", "stabilizing": "Böyle kalın", "pose_not_clear": "Görüntü net değil",
            "valid": "Analiz ediliyor", "too_far": "Yaklaşın", "too_close": "Uzaklaşın",
            "move_left": "Sola bir adım", "move_right": "Sağa bir adım", "body_not_visible": "Tam boy görünün",
            "pose_not_found": "Kadraja girin", "face_camera": "Kameraya dönün", "capturing_photo": "Fotoğraf çekiliyor",
        },
        "res_title": "Kontrol sonucun",
        "res_today": "Bugünkü ölçüm · {date}",
        "top_one": "Ölçümde en belirgin alan",
        "top_n": "Ölçümde en belirgin {count} alan",
        "tag1": "Ölçümde en belirgin", "tag2": "Ölçümde ikinci",
        "locked": "Günlük hayatta ne zaman görülür ve planın ne yapıyor",
        "strong_title": "Güçlü yanın",
        "no_findings": "Bu kontrolde öne çıkan bir alan görülmedi.",
        "disclaimer": "PosMetric tıbbi tanı koymaz, tedavi önermez.",
        "front": "Önden",
        "name_head": "Yana eğik baş", "name_sh": "Omuz yükseklik farkı",
        "dir_left": "sola", "dir_right": "sağa",
        "side_left": "Sol", "side_right": "Sağ",
        "head_tilt": "Başın {direction} doğru biraz eğik duruyor.",
        "head_strong": "Başın dik ve ortada duruyor.",
        "sh_tilt": "{highSide} omzun diğerinden biraz yukarıda duruyor.",
        "sh_strong": "Omuzların aynı yükseklikte duruyor.",
    },
    "en": {
        "title": "Mini check — PosMetric",
        "desc": "Stand in front of your camera; your coach guides you by voice and the measurement happens on its own. The image never leaves your device.",
        "eyebrow": "Try it in your browser",
        "h1": "Mini check",
        "lead": "A small taste of the app's front photo. Your coach guides you by voice; once you're standing right, the measurement happens on its own.",
        "privacy": "The image never leaves your device. The measurement runs in your browser; nothing is sent or saved.",
        "pick": "Pick your coach",
        "sound": "Voice guidance",
        "tips_title": "How to stand",
        "tips": [
            "Put your computer or phone somewhere around waist height.",
            "Step back a few paces so you're visible from head to ankles.",
            "Face the camera with your arms relaxed at your sides.",
            "Keep the light in front of you, not a window behind you.",
        ],
        "start": "Start the check",
        "again": "Measure again",
        "loading": "Getting ready…",
        "cam_error": "The camera couldn't start. Check your browser's camera permission, or do the full check in the app.",
        "unsupported": "This browser can't run the mini check. You can do the full check in the app.",
        "app_title": "What's waiting for you in the app?",
        "app_lead": "This measurement used the same system as the app. The app has more:",
        "free_tag": "Free",
        "app_items": [
            ("📐", "The full check", "Two photos, front and side, cover 23 areas; here you saw just 2.", False),
            ("🎯", "A plan built around you", "A 3-movement plan that gives priority to the areas that stood out in your measurement.", True),
            ("🗣️", "Your coach by your side", "{fem} or {mal} does every move with you and counts out loud.", False),
            ("☕", "Desk break", "3 short moves right where you sit.", True),
            ("🔥", "Rings and streaks", "Your rings fill up on every day you move.", True),
        ],
        "cta_title": "The full check and your plan are in the app",
        "live": {
            "moving": "Hold still", "stabilizing": "Stay like this", "pose_not_clear": "Image not clear",
            "valid": "Analyzing", "too_far": "Move closer", "too_close": "Step back",
            "move_left": "Step left", "move_right": "Step right", "body_not_visible": "Show full body",
            "pose_not_found": "Step into frame", "face_camera": "Face the camera", "capturing_photo": "Taking photo",
        },
        "res_title": "Your check result",
        "res_today": "Today's measurement · {date}",
        "top_one": "The area that stood out most",
        "top_n": "The {count} areas that stood out most",
        "tag1": "Stood out most", "tag2": "Second in the measurement",
        "locked": "When it shows up in daily life and what your plan does",
        "strong_title": "Your strong side",
        "no_findings": "No area stood out in this check.",
        "disclaimer": "PosMetric does not diagnose or recommend treatment.",
        "front": "Front",
        "name_head": "Head tilted sideways", "name_sh": "Shoulder height difference",
        "dir_left": "to the left", "dir_right": "to the right",
        "side_left": "left", "side_right": "right",
        "head_tilt": "Your head tilts a little {direction}.",
        "head_strong": "Your head sits straight and centered.",
        "sh_tilt": "Your {highSide} shoulder sits a little higher than the other.",
        "sh_strong": "Your shoulders sit at the same height.",
    },
    "de": {
        "title": "Mini-Check — PosMetric",
        "desc": "Stell dich vor deine Kamera; dein Coach leitet dich mit der Stimme an und die Messung startet von selbst. Das Bild verlässt dein Gerät nicht.",
        "eyebrow": "Im Browser ausprobieren",
        "h1": "Mini-Check",
        "lead": "Ein kleiner Vorgeschmack auf das Frontfoto der App. Dein Coach leitet dich mit der Stimme an; sobald du richtig stehst, startet die Messung von selbst.",
        "privacy": "Das Bild verlässt dein Gerät nicht. Die Messung läuft in deinem Browser; nichts wird gesendet oder gespeichert.",
        "pick": "Wähl deinen Coach",
        "sound": "Sprachführung",
        "tips_title": "So stellst du dich hin",
        "tips": [
            "Stell deinen Computer oder dein Handy etwa auf Hüfthöhe.",
            "Geh ein paar Schritte zurück, sodass du vom Kopf bis zu den Knöcheln zu sehen bist.",
            "Schau frontal in die Kamera, die Arme locker neben dem Körper.",
            "Das Licht sollte von vorn kommen, kein Fenster hinter dir.",
        ],
        "start": "Check starten",
        "again": "Noch einmal messen",
        "loading": "Wird vorbereitet…",
        "cam_error": "Die Kamera ließ sich nicht starten. Prüf die Kameraberechtigung deines Browsers oder mach den vollständigen Check in der App.",
        "unsupported": "Dieser Browser kann den Mini-Check nicht ausführen. Den vollständigen Check kannst du in der App machen.",
        "app_title": "Was dich in der App erwartet",
        "app_lead": "Diese Messung lief mit demselben System wie in der App. Die App kann noch mehr:",
        "free_tag": "Kostenlos",
        "app_items": [
            ("📐", "Der vollständige Check", "Zwei Fotos, von vorn und von der Seite, decken 23 Bereiche ab; hier hast du nur 2 gesehen.", False),
            ("🎯", "Ein Plan, der zu dir passt", "Ein Plan mit 3 Übungen, der die auffälligsten Bereiche deiner Messung zuerst angeht.", True),
            ("🗣️", "Dein Coach an deiner Seite", "{fem} oder {mal} macht jede Übung mit dir und zählt laut mit.", False),
            ("☕", "Schreibtischpause", "3 kurze Übungen direkt am Platz.", True),
            ("🔥", "Ringe und Serien", "An jedem Tag, an dem du dich bewegst, füllen sich deine Ringe.", True),
        ],
        "cta_title": "Vollständiger Check und dein Plan in der App",
        "live": {
            "moving": "Stillhalten", "stabilizing": "So bleiben", "pose_not_clear": "Bild unscharf",
            "valid": "Analyse läuft", "too_far": "Näher kommen", "too_close": "Zurücktreten",
            "move_left": "Schritt nach links", "move_right": "Schritt nach rechts", "body_not_visible": "Ganz ins Bild",
            "pose_not_found": "Ins Bild treten", "face_camera": "Zur Kamera drehen", "capturing_photo": "Foto wird gemacht",
        },
        "res_title": "Dein Check-Ergebnis",
        "res_today": "Heutige Messung · {date}",
        "top_one": "Der auffälligste Bereich der Messung",
        "top_n": "Die {count} auffälligsten Bereiche der Messung",
        "tag1": "Am auffälligsten", "tag2": "An zweiter Stelle",
        "locked": "Wann es im Alltag auftritt und was dein Plan dafür tut",
        "strong_title": "Deine Stärke",
        "no_findings": "Bei diesem Check ist kein Bereich aufgefallen.",
        "disclaimer": "PosMetric stellt keine Diagnosen und empfiehlt keine Behandlung.",
        "front": "Von vorn",
        "name_head": "Seitlich geneigter Kopf", "name_sh": "Unterschiedliche Schulterhöhe",
        "dir_left": "nach links", "dir_right": "nach rechts",
        "side_left": "links", "side_right": "rechts",
        "head_tilt": "Dein Kopf ist etwas {direction} geneigt.",
        "head_strong": "Dein Kopf steht gerade und mittig.",
        "sh_tilt": "Deine Schulter ({highSide}) steht etwas höher als die andere.",
        "sh_strong": "Deine Schultern stehen auf gleicher Höhe.",
    },
    "es": {
        "title": "Minicontrol — PosMetric",
        "desc": "Ponte frente a la cámara; tu coach te guía con la voz y la medición se hace sola. La imagen no sale de tu dispositivo.",
        "eyebrow": "Pruébalo en tu navegador",
        "h1": "Minicontrol",
        "lead": "Una pequeña muestra de la foto de frente de la app. Tu coach te guía con la voz y, cuando estás bien colocado, la medición se hace sola.",
        "privacy": "La imagen no sale de tu dispositivo. La medición se hace en tu navegador; no se envía ni se guarda nada.",
        "pick": "Elige a tu coach",
        "sound": "Guía por voz",
        "tips_title": "Cómo colocarte",
        "tips": [
            "Pon el ordenador o el móvil más o menos a la altura de la cintura.",
            "Da unos pasos atrás para que se te vea de la cabeza a los tobillos.",
            "Mira de frente a la cámara, con los brazos relajados a los lados.",
            "Que la luz te llegue de frente, sin una ventana detrás.",
        ],
        "start": "Empezar el control",
        "again": "Medir de nuevo",
        "loading": "Preparando…",
        "cam_error": "No se pudo activar la cámara. Revisa el permiso de cámara de tu navegador o haz el control completo en la app.",
        "unsupported": "Este navegador no puede ejecutar el minicontrol. Puedes hacer el control completo en la app.",
        "app_title": "¿Qué te espera en la app?",
        "app_lead": "Esta medición usó el mismo sistema que la app. En la app hay más:",
        "free_tag": "Gratis",
        "app_items": [
            ("📐", "El control completo", "Dos fotos, de frente y de lado, cubren 23 zonas; aquí has visto solo 2.", False),
            ("🎯", "Un plan a tu medida", "Un plan de 3 movimientos que da prioridad a las zonas más marcadas de tu medición.", True),
            ("🗣️", "Tu coach a tu lado", "{fem} o {mal} hace cada movimiento contigo y cuenta en voz alta.", False),
            ("☕", "Pausa de escritorio", "3 movimientos cortos sin levantarte.", True),
            ("🔥", "Anillos y rachas", "Tus anillos se llenan cada día que te mueves.", True),
        ],
        "cta_title": "El control completo y tu plan, en la app",
        "live": {
            "moving": "No se mueva", "stabilizing": "Así, sin moverse", "pose_not_clear": "Imagen borrosa",
            "valid": "Analizando", "too_far": "Acérquese", "too_close": "Aléjese",
            "move_left": "Paso a la izquierda", "move_right": "Paso a la derecha", "body_not_visible": "Cuerpo entero",
            "pose_not_found": "Entre en cuadro", "face_camera": "Mire a la cámara", "capturing_photo": "Tomando foto",
        },
        "res_title": "El resultado de tu revisión",
        "res_today": "Medición de hoy · {date}",
        "top_one": "La zona más marcada de la medición",
        "top_n": "Las {count} zonas más marcadas de la medición",
        "tag1": "La más marcada", "tag2": "La segunda",
        "locked": "Cuándo aparece en el día a día y qué hace tu plan",
        "strong_title": "Tu punto fuerte",
        "no_findings": "En esta revisión no destacó ninguna zona.",
        "disclaimer": "PosMetric no hace diagnósticos ni recomienda tratamientos.",
        "front": "De frente",
        "name_head": "Cabeza inclinada de lado", "name_sh": "Diferencia de altura de los hombros",
        "dir_left": "hacia la izquierda", "dir_right": "hacia la derecha",
        "side_left": "izquierdo", "side_right": "derecho",
        "head_tilt": "Tu cabeza está un poco inclinada {direction}.",
        "head_strong": "Tu cabeza está recta y centrada.",
        "sh_tilt": "Tu hombro del lado {highSide} está un poco más alto que el otro.",
        "sh_strong": "Tus hombros están a la misma altura.",
    },
}
