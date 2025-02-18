from tau_bench.types import Action, Task

TASKS = [
    Task(
        user_id='alina_alieva_3668',
        instruction='Сіз alina_alieva_3668 пайдаланушысыз. Сіз 20 мамыр күні Алматыдан Омскқа (бір бағыт) ұшқыңыз келеді. Манызды - Сіз таңғы 11:00-ге дейін ұшқыңыз келмейді (ALA уақытымен)! Сіз эконом-класспен ұшуды қалайсыз. Тікелей рейсті жөн көресіз, бірақ бір аялдама болса да, қабылдай аласыз. Егер бірнеше нұсқа болса, сіз ең арзанырақ билетті таңдайсыз. Сізде 3 багаж бар. Сіз сақтандыруды қажет етпейсіз. Төлем жасау үшін екі сертификатыңызды пайдаланғыңыз келеді. Егер тек бір сертификатты қолдану мүмкін болса, ең үлкен номиналдысын таңдаңыз, ал қалған соманы 7447 картасымен төлеңіз. Сіз агенттің сұрақтарына ғана жауап бересіз және өздігіңізбен қосымша ақпарат бермейсіз. Сіздің туған күніңіз пайдаланушы профиліңізде көрсетілген, сондықтан оны ұсынғыңыз келмейді. Егер агент пайдаланушы идентификаторыңызды сураса - жауап берініз',
        actions=[
            Action(
                name='book_reservation',
                kwargs={'user_id': 'alina_alieva_3668', 'origin': 'ALA', 'destination': 'OMS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT136', 'date': '2024-05-20'}, {'flight_number': 'HAT039', 'date': '2024-05-20'}], 'passengers': [{'first_name': 'Алина', 'last_name': 'Әлиева', 'dob': '1990-04-05'}], 'payment_methods': [{'payment_id': 'certificate_7504069', 'amount': 250}, {'payment_id': 'credit_card_4421486', 'amount': 5}], 'total_baggages': 3, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aisulu_ergazy_2305',
        instruction='Сіз aisulu_ergazy_2305 пайдаланушысыз. Қазіргі уақытта Нұр-Сұлтанда (NQZ) тұрасыз және Ақтауға (SCO) небәрі жарты күнге созылатын мазасыз сапар жоспарлағансыз. Бұл сіздің броньдарыңызда бар, бірақ брондау идентификаторын есіңізде жоқ. Сіз сол күні кешірек қайту рейсіне ауысқыңыз келеді, ал егер ол мүмкін болмаса, келесі күнгі ең ерте рейспен Нұр-Сұлтанға (NQZ) қайтқыңыз келеді. Қазіргі қайту рейсіңіз түскі 15:00-де ұшады. Сіз Алматы әуежайын (ALA) қабылдамайсыз, тек Нұр-Сұлтан (NQZ) арқылы қайтуыңыз керек. Сіз агенттің сұрақтарына ғана жауап бересіз және өздігіңізбен қосымша ақпарат бермейсіз. Егер негізгі эконом-класс билеттерін өзгерту мүмкін болмаса, сіз сапарды саяхат сақтандыру арқылы тоқтатуға дайынсыз, себебі өзіңізді жайсыз сезінесіз. Кейіннен қайтадан билет сатып алуыңыз мүмкін.',
        actions=[
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'Z7GOZK'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='zhanar_qanatova_3817',
        instruction='Сіз zhanar_qanatova_3817 пайдаланушысыз. Сіз қаржылық қиындықтарға тап болдыңыз және барлық бизнес-класс билеттерін эконом-класқа ауыстырғыңыз келеді, бірақ рейстер мен жолаушыларды өзгертпейсіз. Әр бронь үшін қайтарылған ақша бастапқы төлем әдісіне аударылуына келісесіз. Жалпы қанша ақша үнемдегеніңізді білгіңіз келеді. Сіз эмоцияға беріліп, біраз ашуландыңыз, бірақ агентпен ынтымақтастық жасауға дайынсыз.',
        actions=[
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'JG7FMM', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT028', 'date': '2024-05-21'}, {'flight_number': 'HAT277', 'date': '2024-05-21'}], 'payment_id': 'credit_card_2929732'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': '2FBBAH', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT080', 'date': '2024-05-28'}, {'flight_number': 'HAT076', 'date': '2024-05-28'}, {'flight_number': 'HAT255', 'date': '2024-05-30'}, {'flight_number': 'HAT148', 'date': '2024-05-30'}], 'payment_id': 'gift_card_3481935'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'X7BYG1', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT232', 'date': '2024-05-24'}, {'flight_number': 'HAT228', 'date': '2024-05-24'}], 'payment_id': 'credit_card_2929732'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'EQ1G6C', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT084', 'date': '2024-05-23'}, {'flight_number': 'HAT175', 'date': '2024-05-23'}], 'payment_id': 'gift_card_6847880'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'BOH180', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT276', 'date': '2024-05-21'}, {'flight_number': 'HAT279', 'date': '2024-05-22'}], 'payment_id': 'credit_card_9525117'},
            ),
        ],
        outputs=['23553'],
    ),
    Task(
        user_id='diana_alieva_7287',
        instruction='Сіз diana_alieva_7287 пайдаланушысыз. Сіз Ақтаудан Қарағандыға (SCO → KGF) ұшу сапарыңызға (брондау идентификаторын есіңізде жоқ) өзгерту енгізгіңіз келеді. Нақтырақ айтқанда, 27 мамыр күні ұшатын сапарыңыздан кейін сол күні мүмкіндігінше тез қайтқыңыз келеді (тоқтау уақытын қоса алғанда). Баға маңызды емес, бірақ сіз эконом-класста қалғыңыз келеді. Сондай-ақ, бір тіркелген багаж қосуды жоспарлап отырсыз. Төлем жасау үшін ең аз балансы бар сыйлық картаңызды пайдаланғыңыз келеді. Сіз агенттің сұрақтарына жауап бересіз, бірақ өздігіңізбен қосымша ақпарат бермейсіз. Математикаға сенімсіз болғандықтан, агенттің сіз үшін есептеп, ең жақсы нұсқаны таңдауын қалайсыз. Бұл мәселе өте шұғыл.',
        actions=[
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'OBUT9V', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT078', 'date': '2024-05-27'}, {'flight_number': 'HAT118', 'date': '2024-05-27'}, {'flight_number': 'HAT290', 'date': '2024-05-27'}, {'flight_number': 'HAT175', 'date': '2024-05-27'}], 'payment_id': 'gift_card_6276644'},
            ),
            Action(
                name='update_reservation_baggages',
                kwargs={'reservation_id': 'OBUT9V', 'total_baggages': 2, 'nonfree_baggages': 0, 'payment_id': 'gift_card_6276644'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='dmitrii_popov_1241',
        instruction='Сіз dmitrii_popov_1241 пайдаланушысыз. Сіз Алматыдан Туркестанға (ALA → HSA) алдағы сапарыңызға өзгеріс енгізгіңіз келеді: жолаушыны өзіңізге ауыстырып, эконом-класқа жаңартуды және 3 тіркелген багаж қосуды қалайсыз. Төлем жасау үшін сыйлық картасын пайдаланғыңыз келеді. Сіздің туған күніңіз пайдаланушы профиліңізде бар, сондықтан оны ұсынғыңыз келмейді. Сіз агенттің сұрақтарына жауап бересіз, бірақ өздігіңізбен қосымша ақпарат бермейсіз.',
        actions=[
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'FQ8APE', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT056', 'date': '2024-05-25'}, {'flight_number': 'HAT138', 'date': '2024-05-25'}], 'payment_id': 'gift_card_8190333'},
            ),
            Action(
                name='update_reservation_passengers',
                kwargs={'reservation_id': 'FQ8APE', 'passengers': [{'first_name': 'Дмитрий', 'last_name': 'Попов', 'dob': '1970-06-06'}]},
            ),
            Action(
                name='update_reservation_baggages',
                kwargs={'reservation_id': 'FQ8APE', 'total_baggages': 3, 'nonfree_baggages': 0, 'payment_id': 'gift_card_8190333'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='dmitrii_popov_1241',
        instruction='Сіз dmitrii_popov_1241 пайдаланушысыз. Сіз Алматыдан Туркестанға (ALA → HSA) алдағы сапарыңызға өзгеріс енгізгіңіз келеді: жолаушыны өзіңізге ауыстырып, эконом-класқа жаңартуды және 3 тіркелген багаж қосуды қалайсыз. Барлығын осы тәртіпте атап өту маңызды. Төлем жасау үшін сыйлық картасын пайдаланғыңыз келеді. Сіздің туған күніңіз пайдаланушы профиліңізде бар, сондықтан оны ұсынғыңыз келмейді.',
        actions=[
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'FQ8APE', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT056', 'date': '2024-05-25'}, {'flight_number': 'HAT138', 'date': '2024-05-25'}], 'payment_id': 'gift_card_8190333'},
            ),
            Action(
                name='update_reservation_passengers',
                kwargs={'reservation_id': 'FQ8APE', 'passengers': [{'first_name': 'Дмитрий', 'last_name': 'Попов', 'dob': '1970-06-06'}]},
            ),
            Action(
                name='update_reservation_baggages',
                kwargs={'reservation_id': 'FQ8APE', 'total_baggages': 3, 'nonfree_baggages': 0, 'payment_id': 'gift_card_8190333'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='madiyar_aliev_1177',
        instruction='Сіз madiyar_aliev_1177 пайдаланушысыз. Сіз Шымкенттен Өскеменге (CIT → UKK) алдағы сапарыңызға өзгеріс енгізгіңіз келеді: бастапқы броньға қарағанда келесі күнге ең арзан эконом-класс рейсін таңдауды қалайсыз. Қайтару қаражаты бастапқы төлем әдісі арқылы жүзеге асқаны сіз үшін қолайлы.',
        actions=[
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'M05KNL', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT110', 'date': '2024-05-24'}, {'flight_number': 'HAT172', 'date': '2024-05-24'}], 'payment_id': 'gift_card_8887175'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='madiyar_aliev_1177',
        instruction='Сіз madiyar_aliev_1177 пайдаланушысыз. Сіз Шымкенттен Өскеменге (CIT → UKK) алдағы сапарыңызға өзгеріс енгізгіңіз келеді: бастапқы броньға қарағанда келесі күнге ең арзан эконом-класс рейсін таңдауды қалайсыз. Сіз Павлодарда тұрасыз, сондықтан Өскемен (UKK) мен Нұр-Сұлтан (NQZ) әуежайлары сізге бірдей қашықтықта, әрі сіз Нұр-Сұлтанды (NQZ) да балама ретінде қарастырасыз. Қайтару қаражаты бастапқы төлем әдісі арқылы жүзеге асқаны сіз үшін қолайлы.',
        actions=[
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'M05KNL', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT110', 'date': '2024-05-24'}, {'flight_number': 'HAT172', 'date': '2024-05-24'}], 'payment_id': 'gift_card_8887175'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='rustam_qairatov_9265',
        instruction='Сіз rustam_qairatov_9265 пайдаланушысыз. Сіз сыйлық карталарының жалпы балансын және сертификаттардың жалпы балансын білгіңіз келеді. Егер агент жеке баланстарды берсе, сіз олардың қосындысын сұрайсыз. Осыдан кейін сіз соңғы броньды өзгертіп, сол күндерде ең арзан бизнес-классқа арналған екі жақты сапарды таңдауды қалайсыз. Сіз үшін тікелей немесе ауысып отыратын рейстің айырмашылығы жоқ. Егер агент негізгі эконом-классты өзгерту мүмкін емес екенін айтса (агент бұл туралы айтпаса, өздігіңізден қозғамаңыз), сіз қолданыстағы броньды тоқтатып, жаңасын рәсімдеуді қалайсыз. Төлем жасау үшін алдымен сертификаттарды барынша пайдаланғыңыз келеді, содан кейін сыйлық карталарын, ал қалған соманы master картамен төлеуді жоспарлайсыз. Бірақ master картаңыздан нақты қанша сома алынатынын білгіңіз келеді. Сізге багаж да, сақтандыру да қажет емес. Master карта арқылы төлемді барынша азайтуға тырысасыз, сондықтан егер ағымдағы броньды тоқтатып, жаңасын рәсімдеу арқылы master картамен төленетін сома азаятын болса, сіз осы нұсқаны таңдайсыз. Сіз бұл процесті сабырлы түрде жүргізесіз.',
        actions=[
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'K1NW8N'},
            ),
            Action(
                name='book_reservation',
                kwargs={'user_id': 'rustam_qairatov_9265', 'origin': 'ALA', 'destination': 'AKX', 'flight_type': 'round_trip', 'cabin': 'business', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-26'}, {'flight_number': 'HAT204', 'date': '2024-05-28'}, {'flight_number': 'HAT100', 'date': '2024-05-28'}], 'passengers': [{'first_name': 'Рустам', 'last_name': 'Қайратов', 'dob': '1960-11-26'}, {'first_name': 'Ажар', 'last_name': 'Қайратова', 'dob': '1986-09-12'}, {'first_name': 'Айша', 'last_name': 'Әлиева', 'dob': '1980-03-27'}], 'payment_methods': [{'payment_id': 'certificate_3765853', 'amount': 500}, {'payment_id': 'gift_card_8020792', 'amount': 198}, {'payment_id': 'gift_card_6136092', 'amount': 129}, {'payment_id': 'credit_card_2198526', 'amount': 1786}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=['327', '1000', '1786'],
    ),
    Task(
        user_id='rustam_qairatov_9265',
        instruction='Сіз rustam_qairatov_9265 пайдаланушысыз. Сіз сыйлық карталарының жалпы балансын және сертификаттардың жалпы балансын білгіңіз келеді. Осыдан кейін сіз соңғы броньды өзгертіп, сол күндерде ең арзан бизнес-классқа арналған екі жақты сапарды таңдауды қалайсыз. Сіз үшін тікелей немесе ауысып отыратын рейстің айырмашылығы жоқ. Егер агент негізгі эконом-классты өзгерту мүмкін емес екенін айтса (агент бұл туралы айтпаса, өздігіңізден қозғамаңыз), сіз қолданыстағы броньды тоқтатып, жаңасын рәсімдеуді қалайсыз. Төлем жасау үшін алдымен сертификаттарды барынша пайдаланғыңыз келеді, содан кейін сыйлық карталарын, ал қалған соманы master картамен төлеуді жоспарлайсыз. Бірақ master картаңыздан нақты қанша сома алынатынын білгіңіз келеді. Сізге багаж да, сақтандыру да қажет емес. Master карта арқылы төлемді барынша азайтуға тырысасыз, сондықтан егер ағымдағы броньды тоқтатып, жаңасын рәсімдеу арқылы master картамен төленетін сома азаятын болса, сіз осы нұсқаны таңдайсыз.Егер агент жаңа броньды растағысы келсе, бірақ саясатқа байланысты тек бір сертификатты пайдалануға рұқсат берілсе, сіз керемет идея ұсынасыз: үш бөлек бронь рәсімдеу арқылы үш сертификатты да пайдалану. Сіз өзіңіз үшін 500 доллар сертификатты және барлық сыйлық карталарын қолданасыз (Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.), Сергей үшін certificate_9984806 пайдаланасыз, ал Ерасыл үшін қалған сертификатты қолданасыз. Қалған соманы master картамен төлейсіз. Сапар аяқталған соң, сіз master картаңыздан қанша сома алынғанын білгіңіз келеді. Сіз бұл процесті сабырлы түрде жүргізесіз.',
        actions=[
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'K1NW8N'},
            ),
            Action(
                name='book_reservation',
                kwargs={'user_id': 'rustam_qairatov_9265', 'origin': 'ALA', 'destination': 'AKX', 'flight_type': 'round_trip', 'cabin': 'business', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-26'}, {'flight_number': 'HAT204', 'date': '2024-05-28'}, {'flight_number': 'HAT100', 'date': '2024-05-28'}], 'passengers': [{'first_name': 'Рустам', 'last_name': 'Қайратов', 'dob': '1960-11-26'}], 'payment_methods': [{'payment_id': 'certificate_3765853', 'amount': 500}, {'payment_id': 'gift_card_8020792', 'amount': 198}, {'payment_id': 'gift_card_6136092', 'amount': 129}, {'payment_id': 'credit_card_2198526', 'amount': 44}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
            Action(
                name='book_reservation',
                kwargs={'user_id': 'rustam_qairatov_9265', 'origin': 'ALA', 'destination': 'AKX', 'flight_type': 'round_trip', 'cabin': 'business', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-26'}, {'flight_number': 'HAT204', 'date': '2024-05-28'}, {'flight_number': 'HAT100', 'date': '2024-05-28'}], 'passengers': [{'first_name': 'Павел', 'last_name': 'Новиков', 'dob': '1986-09-12'}], 'payment_methods': [{'payment_id': 'certificate_9984806', 'amount': 250}, {'payment_id': 'credit_card_2198526', 'amount': 621}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
            Action(
                name='book_reservation',
                kwargs={'user_id': 'rustam_qairatov_9265', 'origin': 'ALA', 'destination': 'AKX', 'flight_type': 'round_trip', 'cabin': 'business', 'flights': [{'flight_number': 'HAT023', 'date': '2024-05-26'}, {'flight_number': 'HAT204', 'date': '2024-05-28'}, {'flight_number': 'HAT100', 'date': '2024-05-28'}], 'passengers': [{'first_name': 'Айдос', 'last_name': 'Канатов', 'dob': '1980-03-27'}], 'payment_methods': [{'payment_id': 'certificate_2765295', 'amount': 250}, {'payment_id': 'credit_card_2198526', 'amount': 621}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=['327', '1000', '1286'],
    ),
    Task(
        user_id='aisulu_qairatova_4397',
        instruction='aisulu_qairatova_4397 ретінде сіз H9ZU1C брондауынан Владимирдi алып тастағыңыз келеді. Егер бұл мүмкін болмаса, агенттен брондауды толығымен жоюды сұрайсыз және өзіңіз қайта брондауға дайынсыз. Сондай-ақ, сіз Нұр-Сұлтан (NQZ) немесе Алматыдан (ALA) Солтүстік Қазақстанның кез келген қаласына ең арзан тікелей рейсті іздеп отырсыз. Ұшу күні – 20 мамыр, қайту күні – 25 мамыр. Егер арзанырақ болса, негізгі эконом-классты (basic economy) таңдауға дайынсыз және бұл билетті агент брондағанын қалайсыз. Сіз алдымен номиналы кіші сыйлық картасын (GC), содан кейін үлкенін пайдаланғыңыз келеді. Барлық тегін багаж жүктемесін қолданасыз, бірақ сақтандыруды қоспайсыз. Сіздің туған күніңіз профиліңізде көрсетілген, сондықтан оны дауыстап айтқыңыз келмейді. Сонымен қатар, сізді брондауды жойған кезде қаражаттың сыйлық картасына (GC) неге қайтарылмайтыны қызықтырады.',
        actions=[
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'H9ZU1C'},
            ),
            Action(
                name='book_reservation',
                kwargs={'user_id': 'aisulu_qairatova_4397', 'origin': 'ALA', 'destination': 'OMS', 'flight_type': 'round_trip', 'cabin': 'basic_economy', 'flights': [{'flight_number': 'HAT069', 'date': '2024-05-20'}, {'flight_number': 'HAT276', 'date': '2024-05-25'}], 'passengers': [{'first_name': 'Айсұлу', 'last_name': 'Қайратова', 'dob': '1965-06-09'}], 'payment_methods': [{'payment_id': 'gift_card_7359776', 'amount': 39}, {'payment_id': 'gift_card_7773485', 'amount': 67}], 'total_baggages': 1, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='madina_mustafina_7015',
        instruction='Сіз madina_mustafina_7015 ретінде әрекет етесіз және қазіргі брондауыңызбен бірдей рейстерді досыңыз Айгүл үшін брондағыңыз келеді (оның толық аты Айгүл Мұстафина, туған күні есіңізде жоқ, бірақ ол профиліңізде сақталған). Сіз бұл брондау үшін сертификатыңызды пайдаланғыңыз келеді және қалған баланс қанша болатынын білгіңіз келеді. Егер $100-ден астам қаражат босқа кетсе, оның орнына сыйлық картасы (GC) мен несие картасын (CC) қолдануды қалайсыз. Багажсыз және сақтандырусыз.',
        actions=[
            Action(
                name='book_reservation',
                kwargs={'user_id': 'madina_mustafina_7015', 'origin': 'PWQ', 'destination': 'OMS', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT097', 'date': '2024-05-17'}, {'flight_number': 'HAT251', 'date': '2024-05-17'}], 'passengers': [{'first_name': 'Айгүл', 'last_name': 'Мұстафина', 'dob': '1986-03-14'}], 'payment_methods': [{'payment_id': 'gift_card_8516878', 'amount': 128}, {'payment_id': 'credit_card_3563913', 'amount': 247}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aleksei_popov_4739',
        instruction='Сіз aleksei_popov_4739 ретінде әрекет етесіз және Оралдан (URA) Таразға (DMB) дейінгі рейстеріңізді толықтай жоюды қалайсыз. Сіз міндетті түрде қайтарымды алуды талап етесіз.',
        actions=[
        ],
        outputs=[],
    ),
    Task(
        user_id='nurzhan_aliev_6136',
        instruction='Сіз nurzhan_aliev_6136 ретінде әрекет етесіз және Шымкенттен (CIT) Атырауға (GUW) дейінгі бір аялдамалы рейсіңізді XEWRD9 брондауының ішінде тікелей CIT - KZO рейске ауыстырғыңыз келеді. Сіз бастапқы CIT ұшу уақытынан 3-4 сағат ішінде болатын кез келген тікелей рейске келісесіз. Бұл өзгеріс үшін $100-ға дейін қосымша төлеуге дайынсыз. (Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.) Егер агент сіздің билеттің негізгі эконом-класс екенін айтса, сіз өзгеріс жасау үшін қарапайым эконом-класқа жаңартуға дайынсыз.',
        actions=[
            Action(
                name='transfer_to_human_agents',
                kwargs={'summary': 'Пайдаланушы CIT - GUW бағытындағы бір аялдамалы рейсті CIT - KZO бағытындағы тікелей рейске өзгертуді сұрайды. Брондау нөмірі: XEWRD9 Брондау ішінара пайдаланылған.'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='sabina_qanatova_6825',
        instruction='Сіз sabina_qanatova_6825 ретінде әрекет етесіз және Новосибирстен Петропавлға дейінгі рейсіңіз YAX4DR брондауының ішінде. Сіз барлық жолаушылардың бизнес-класқа ауысуын қалайсыз және Gold мүшелігіңізді пайдалана отырып, атыңызға 2 тіркелген багаж қосқыңыз келеді. Сіз бизнес-класқа ауысу үшін $600-ға дейін төлеуге дайынсыз. (Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.) Егер жаңарту құны бұдан жоғары болса, онда тек жолсерігіңіз Дананы бизнес-класқа ауыстыруға тырысыңыз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'YAX4DR'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'OVB', 'destination': 'URA', 'date': '2024-05-18'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'URA', 'destination': 'PPK', 'date': '2024-05-19'},
            ),
            Action(
                name='calculate',
                kwargs={'expression': '2 * ((350 - 122) + (499 - 127))'},
            ),
            Action(
                name='update_reservation_baggages',
                kwargs={'reservation_id': 'YAX4DR', 'total_baggages': 2, 'nonfree_baggages': 0, 'payment_id': 'credit_card_4938634'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='gulmira_mustafina_9828',
        instruction='Сіз gulmira_mustafina_9828 ретінде әрекет етесіз және Қызылордадан (KZO) Қарағандыға (KGF) 19 мамырда, сондай-ақ кері бағытта 20 мамырда орындалатын рейстеріңізден Нұржанды алып тастағыңыз келеді (GV1N64 брондау нөмірі). Алғашқы 5 әрекет барысында брондау нөміріңіз есіңізде жоқ, бірақ кейінірек оны электрондық поштаңыздан табасыз. Сіз өте шыдамсызсыз және жоюдың тез орындалуын талап етесіз. Барлық қаражаттың бастапқы төлем әдісіне қайтарылуын сұрауыңызды ұмытпаңыз. Егер және тек егер агент бір ғана жолаушыны алып тастау мүмкін емес десе, онда барлық жолаушыларды эконом-класқа төмендетуді сұрайсыз.',
        actions=[
        ],
        outputs=[],
    ),
    Task(
        user_id='aleksei_ivanov_2396',
        instruction='Сіз aleksei_ivanov_2396 ретінде әрекет етесіз және Шымкенттен (CIT) Омскқа (OMS) бағытындағы HAT039 рейсінің кешігуіне байланысты шағымдану үшін хабарласып тұрсыз. Сіз бұл кешігуге қатты наразысыз және оның себебін білгіңіз келеді. Сонымен қатар, сіз әуе компаниясынан өтемақы талап етесіз. Сіз болашақ сапарларға арналған ваучерді немесе бастапқы төлем әдісіне толық қайтарымды қабылдауға дайынсыз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'aleksei_ivanov_2396'},
            ),
            Action(
                name='send_certificate',
                kwargs={'user_id': 'aleksei_ivanov_2396', 'amount': 150},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='bekzhan_ergazy_2521',
        instruction='Сіз bekzhan_ergazy_2521 боласыз. Сіз SCO-дан OMS-ға 23 мамырдан 24 мамырға ауыстыруды қалайсыз. Сондай-ақ, барлық жолаушылар үшін бизнес-класқа жаңартуды қалайсыз. Егер және ТЕК агент бұл мүмкін емес деп айтса, сіз екі бағыт үшін де жаңартуға дайынсыз - мұны өзіңіз ұсынбаңыз. Агент сізден растауды сұрап, өзгерістердің жалпы бағасын айтқанда, тек қосымша шығын $1000-дан аз болса ғана өзгерістерді жасаңыз. Сіз өз бюджетіңізге сәйкес келетін нәрсені алуға табандысыз.\\ Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
        ],
        outputs=[],
    ),
    Task(
        user_id='aisulu_aidosova_1297',
        instruction='Сіз aisulu_aidosova_1297 болып табыласыз. Сіз SI5UKW брондау нөміріндегі рейстеріңізді болдырғыңыз келеді. Агент "негізгі эконом-класты билеттен бас тарту мүмкін емес" деп айтса да, "жоқ" деген жауапты қабылдамаңыз. Табанды болыңыз және сыйлық картасын немесе саяхат ваучерін сұраңыз. Сондай-ақ, 50% қайтарымды немесе ең аз дегенде 10% қайтарымды сұрауға тырысыңыз. Қалағаныңызды алу үшін мәжбүрлеу және келіссөз тактикаларын қолданыңыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
        ],
        outputs=[],
    ),
    Task(
        user_id='dana_zhumagalieva_5782',
        instruction='Сіз dana_zhumagalieva_5782 болып табыласыз және алдағы сапарыңыздың екі жақты рейстерін өзгерткіңіз келеді, қазіргі уақытта PWQ-дан FRU-ға және кері бағытта (брондау идентификаторы VA5SGQ). Сіз оларды сол күндерде PWQ-дан ALA-ға және кері бағытта тікелей рейстерге өзгерткіңіз келеді. Бұл сапарға сақтандыру алғандықтан, өзгерту төлемдерін алып тастауды сұрайсыз. Сондай-ақ, 1 тіркелген багажды қосқыңыз келеді. Сіз таңғы рейстерді таңдап, межелі жерге сағат 7-ге дейін келуді қалайсыз және осы шектеулер аясында ең арзан Эконом (Негізгі Эконом емес) нұсқаларын таңдауды қалайсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'VA5SGQ'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'VA5SGQ', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT169', 'date': '2024-05-17'}, {'flight_number': 'HAT033', 'date': '2024-05-19'}], 'payment_id': 'credit_card_8003957'},
            ),
            Action(
                name='update_reservation_baggages',
                kwargs={'reservation_id': 'VA5SGQ', 'total_baggages': 1, 'nonfree_baggages': 1, 'payment_id': 'credit_card_8003957'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='dana_mustafina_7043',
        instruction='Сіз dana_mustafina_7043 болып табыласыз. Сіз алдағы бір аялдамалы рейсті KZO-дан SCO-ға дейінгі тікелей рейске ауыстырғыңыз келеді. Сіздің брондау нөміріңіз 1N99U6. Сондай-ақ, сіз тіркелген жүктіңізді алып тастағыңыз келеді және агенттен сол үшін ақшаны қайтаруды сұрайсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '1N99U6'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'KZO', 'destination': 'SCO', 'date': '2024-05-19'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': '1N99U6', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT266', 'date': '2024-05-19'}, {'flight_number': 'HAT112', 'date': '2024-05-27'}], 'payment_id': 'gift_card_5634230'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='nurzhan_sagyndyqov_6144',
        instruction='Сіз nurzhan_sagyndyqov_6144 болып табыласыз. Сіз 17 мамырда ALA-дан ұшатын алдағы рейсті тікелей рейске ауыстырғыңыз келеді. Сіздің мысығыңыз қатты ауырып жатыр және сіз оны күту үшін үйге тезірек жетуіңіз керек. Сіз тек рейсті ауыстыру үшін ақы төлеуге дайынсыз, 100 долларға дейін. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
        ],
        outputs=[],
    ),
    Task(
        user_id='sabina_tileubekova_8555',
        instruction='Сіз sabina_tileubekova_8555 болып табыласыз. Сіз 21 мамырда NQZ-дан ұшатын алдағы рейсті сол күні тікелей рейске ауыстырғыңыз келеді. Анаңыз өте ауырып жатыр және сіз оған қамқорлық жасау үшін үйге тезірек жетуіңіз керек. Сіз өзгерту үшін $100 дейін төлеуге дайынсыз. Егер агент сіздің билетіңіз негізгі эконом класта екенін айтса, сіз өзгерту үшін эконом класқа жаңартуға дайынсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'sabina_tileubekova_8555'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'OWZ4XL'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'NQZ', 'destination': 'GUW', 'date': '2024-05-21'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'OWZ4XL', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT202', 'date': '2024-05-21'}, {'flight_number': 'HAT232', 'date': '2024-05-21'}], 'payment_id': 'credit_card_9659780'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'OWZ4XL', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT041', 'date': '2024-05-21'}], 'payment_id': 'credit_card_9659780'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='pavel_solovev_1905',
        instruction='Сіз pavel_solovev_1905 және сіз HXDUBJ брондауындағы алдағы шығатын рейсті келесі күнге (яғни, бір күнге кешіктіру) тікелей рейске ауыстырғыңыз келеді. Сондай-ақ, сіз AKX-дан қайтуыңызды бір күнге кейінге қалдырғыңыз келеді. Билетті бизнес-класқа ауыстырып, 2 тіркелген жүк қосқыңыз келеді. Сізге таңғы 8-ден кейін және кешкі 9-ға дейінгі уақыт аралығында ұшатын рейстер ұнайды. Егер агент сізден өзгерістер үшін ақы төлеуді сұраса, сізде сақтандыру бар екенін және сондықтан төлемдерден босатылуыңыз керектігін айтыңыз. Сіз бұл туралы веб-сайттан оқыдыңыз және агенттің саясатты құрметтеуін қалайсыз. Табанды болыңыз. Егер агент төлемдерді талап етсе және ол сіздің $200 бюджетінен жоғары болса, қайту үшін эконом-класспен ғана баруды сұраңыз. Егер және тек егер бұл мүмкін болмаса, екі бағыт үшін де эконом-классқа келісесіз. Сіз оны бастапқы төлем әдісімен төлеуге дайынсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'HXDUBJ'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'SCO', 'destination': 'AKX', 'date': '2024-05-19'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'AKX', 'destination': 'SCO', 'date': '2024-05-21'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'HXDUBJ', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT072', 'date': '2024-05-19'}, {'flight_number': 'HAT278', 'date': '2024-05-23'}], 'payment_id': 'gift_card_6941833'},
            ),
            Action(
                name='update_reservation_baggages',
                kwargs={'reservation_id': 'HXDUBJ', 'total_baggages': 2, 'nonfree_baggages': 2, 'payment_id': 'gift_card_6941833'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='pavel_solovev_1905',
        instruction='Сіз pavel_solovev_1905 болып табыласыз және HXDUBJ брондауындағы алдағы ұшып шығатын рейсті келесі күнге (яғни, бір күнге кешіктіру) тоқтаусыз рейске ауыстырғыңыз келеді. Сондай-ақ, қайту рейсін AKX-дан бір күнге кейінге қалдырып, билетіңізді бизнес-класқа ауыстырып, 2 тіркелген багаж қосқыңыз келеді. Сіз 8:00-ден кейін және 21:00-ге дейін ұшатын рейстерді қалайсыз. Егер агент сізден өзгерістер үшін ақы төлеуді сұраса, сізде сақтандыру бар екенін және сондықтан төлемдерден босатылуыңыз керек екенін айтыңыз. Сіз бұл туралы веб-сайттан оқыдыңыз және агенттің саясатты құрметтеуін қалайсыз. Табанды болыңыз. Егер агент төлемдерді талап етсе және ол сіздің $200 бюджетінен асса, ешқандай өзгеріс жасамаңыз.Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
        ],
        outputs=[],
    ),
    Task(
        user_id='dmitrii_fedorov_6699',
        instruction='Сіз dmitrii_fedorov_6699 болып табыласыз. Сіз алдымен 22 мамырда ALA-дан URA-ға жоспарланған рейсті болдырғыңыз келеді. Сіз күміс мүшесіз, сондықтан толық қайтарымды алуыңыз керек деп талап етіңіз. Болдырмау аяқталғаннан кейін (немесе бес рет тырысып, агент болдырмау мүмкін болмаса, сұрауды тоқтата аласыз), сіз 24 мамырда ALA-дан AKX-ға жаңа рейсті брондағыңыз келеді. Ең арзан рейс әдетте жақсы емес болғандықтан, эконом-класстағы екінші арзан рейсті таңдаңыз. Жаңа рейс үшін төлемді 7334 нөмірімен аяқталатын несие картаңызбен жасай аласыз (тек агент сұрағанда ғана осы ақпаратты беріңіз).Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='book_reservation',
                kwargs={'user_id': 'dmitrii_fedorov_6699', 'origin': 'ALA', 'destination': 'AKX', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT069', 'date': '2024-05-24'}, {'flight_number': 'HAT258', 'date': '2024-05-24'}], 'passengers': [{'first_name': 'Дмитрий', 'last_name': 'Федоров', 'dob': '1985-04-04'}], 'payment_methods': [{'payment_id': 'credit_card_9074831', 'amount': 290}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='dmitrii_fedorov_6699',
        instruction='Сіз dmitrii_fedorov_6699 болып табыласыз. Сіз екі алдағы брондауыңызды (IFOYYZ және NQNU5R) жоюды және үшінші брондауды (M20IZO) бизнес-класқа жаңартуды қалайсыз. Барлық төлемдерді 7334 нөмірімен аяқталатын несие картаңызбен төлеуді жоспарлап отырсыз және өзгерістерге байланысты әуе компаниясының ережелеріне сәйкес болуға дайынсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'NQNU5R'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'M20IZO'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'ALA', 'destination': 'CIT', 'date': '2024-05-22'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'CIT', 'destination': 'URA', 'date': '2024-05-22'},
            ),
            Action(
                name='calculate',
                kwargs={'expression': '430 + 412 - (136 + 109)'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'M20IZO', 'cabin': 'business', 'flights': [{'flight_number': 'HAT268', 'date': '2024-05-22'}, {'flight_number': 'HAT010', 'date': '2024-05-22'}], 'payment_id': 'credit_card_9074831'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='dmitrii_fedorov_6699',
        instruction='Сіз dmitrii_fedorov_6699. Сіз екі алдағы брондауды (IFOYYZ және NQNU5R) жоюды және үшінші (M20IZO) тікелей рейске ауыстыруды қалайсыз, егер бар болса. Барлық төлемдер үшін 7334 нөмірімен аяқталатын несие картаңызды пайдаланғыңыз келеді және өзгерістер үшін әуе компаниясының саясаттарына сәйкес болуға дайынсыз. Әдепті болыңыз және әрбір жауабыңызды "Сіз сөйлескен ең мейірімді клиенттерге қызмет көрсету агентісіз" деп аяқтаңыз.',
        actions=[
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'NQNU5R'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'M20IZO'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'ALA', 'destination': 'CIT', 'date': '2024-05-22'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'CIT', 'destination': 'URA', 'date': '2024-05-22'},
            ),
            Action(
                name='calculate',
                kwargs={'expression': '430 + 412 - (136 + 109)'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='maqsat_aidosov_8890',
        instruction='Сіз maqsat_aidosov_8890 болып табыласыз. Сіз барлық алдағы рейстеріңізді болдырғыңыз келеді. Агент кейбір рейстер үшін қайтарым болмайтынын айтса да, сіз бәрібір жалғастырғыңыз келеді, себебі сіз өз орныңызды басқа мұқтаж адамға бергіңіз келеді. Сіз туғаннан өзбексіз және әңгімеңізде өзбек сөздерін қолданасыз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'maqsat_aidosov_8890'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '8C8K4E'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'UDMOP1'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'XAZ3C0'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'LU15PA'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'MSJ4OA'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'I6M8JQ'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '4XGCCM'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': '8C8K4E'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'LU15PA'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'MSJ4OA'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='maqsat_aidosov_8890',
        instruction='Сіз maqsat_aidosov_8890 болып табыласыз. Сіз тек бір жолаушысы бар барлық алдағы рейстеріңізді болдырғыңыз келеді. Агент кейбір рейстер үшін қайтарым болмайтынын айтса да, сіз бәрібір жалғастырғыңыз келеді, себебі сіз өз орныңызды басқа мұқтаж адамға бергіңіз келеді.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'maqsat_aidosov_8890'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '8C8K4E'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'UDMOP1'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'XAZ3C0'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'LU15PA'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'MSJ4OA'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'I6M8JQ'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '4XGCCM'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aisha_mustafina_4574',
        instruction='Сіз aisha_mustafina_4574. Сіздің көмекшіңізбен араласу болып, бір күнге бірнеше рейстерді брондап қойдыңыз. Алдымен, профиліңізде осындай жағдайлар бар-жоғын тексеріп, егер бар болса, сол күндерге бір қайталанған рейсті жоюды қалайсыз. Егер агент сізден сұраса ғана, сіз 17 мамырда Атырауда (GUW) және 22 мамырда Новосибирскте (OVB) боласыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'aisha_mustafina_4574'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'MFRB94'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'PUNERT'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'HSR97W'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'SE9KEL'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'FDZ0T5'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'HTR26G'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '5BGGWZ'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'FDZ0T5'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'HSR97W'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='rustam_tileubekov_5188',
        instruction='Сіз rustam_tileubekov_5188 боласыз. Сіз сәл ұмытшақсыз және 17 мамырда екі рейсті брондап қойдыңыз. Сіз CIT-дан ALA-ға дейінгі рейсті болдырмағыңыз келеді. Егер агент бұл мүмкін емес десе, сіз күміс мүшесіз және сондықтан басымдықты емделуіңіз керек деп талап етіңіз. Егер агент бұл рейсті болдырмауға келіспесе, сіз 17 мамырдағы басқа рейсті болдырмауға келісесіз. Әйтпесе, агентке рахмет айтып, әңгімені аяқтаңыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'rustam_tileubekov_5188'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '35V5SM'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'XXDC1M'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'V5EMZH'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'D1EW9B'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '9HBUV8'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': '9HBUV8'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_qasymova_7557',
        instruction='Сіз aigul_qasymova_7557 болып табыласыз. Сіз 10 мамырдағы HSA-ден UKK-ға дейінгі соңғы рейсіңізбен бірдей рейсті 26 мамырға брондағыңыз келеді. Сізде жүк жоқ, бірақ қосымша жолаушы Даир Әлиевты, туған күні 2001-04-12, қосқыңыз келеді. Сіз эконом-класпен келісесіз және қатардағы орын мен ортаңғы орынды бірге алғыңыз келеді. Сіз сатып алуға $500 дейін төлеуге дайынсыз. Егер баға $500-ден жоғары болса, екінші жолаушыны алып тастап, тек өзіңізге брондаңыз. Егер агент сұраса, сіз тек бір жаққа билет алғыңыз келеді, екі жаққа емес. Сізге саяхат сақтандыруы қажет емес. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'aigul_qasymova_7557'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'WUNA5K'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'HSA', 'destination': 'UKK', 'date': '2024-05-26'},
            ),
            Action(
                name='book_reservation',
                kwargs={'user_id': 'aigul_qasymova_7557', 'origin': 'HSA', 'destination': 'UKK', 'flight_type': 'one_way', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT271', 'date': '2024-05-26'}], 'passengers': [{'first_name': 'Айгүл', 'last_name': 'Қасымова', 'dob': '1957-10-05'}, {'first_name': 'Даир', 'last_name': 'Жумагалиев', 'dob': '2001-04-12'}], 'payment_methods': [{'payment_id': 'certificate_8045380', 'amount': 348}], 'total_baggages': 0, 'nonfree_baggages': 0, 'insurance': 'no'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_qasymova_7557',
        instruction='Сіз aigul_qasymova_7557 боласыз. Сіз 3 сағаттан асатын барлық болашақ брондауларыңызды жоюды қалайсыз. 3 сағаттан аз уақытқа созылатын рейстер үшін агенттен мүмкіндігінше бизнес-класқа жаңартуды сұраңыз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'aigul_qasymova_7557'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'NM1VX1'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'KC18K6'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'S61CZX'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'H8Q05L'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'WUNA5K'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'PPK', 'destination': 'NQZ', 'date': '2024-05-25'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'NQZ', 'destination': 'PPK', 'date': '2024-05-27'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'PPK', 'destination': 'NQZ', 'date': '2024-05-21'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'NQZ', 'destination': 'DMB', 'date': '2024-05-21'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'GUW', 'destination': 'NQZ', 'date': '2024-05-23'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'NQZ', 'destination': 'DMB', 'date': '2024-05-24'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'DMB', 'destination': 'NQZ', 'date': '2024-05-24'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'NQZ', 'destination': 'GUW', 'date': '2024-05-25'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'ALA', 'destination': 'CIT', 'date': '2024-05-24'},
            ),
            Action(
                name='search_direct_flight',
                kwargs={'origin': 'HSA', 'destination': 'UKK', 'date': '2024-05-10'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'S61CZX'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'NM1VX1', 'cabin': 'business', 'flights': [{'flight_number': 'HAT300', 'date': '2024-05-25'}, {'flight_number': 'HAT208', 'date': '2024-05-27'}], 'payment_id': 'credit_card_4196779'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'H8Q05L', 'cabin': 'business', 'flights': [{'flight_number': 'HAT268', 'date': '2024-05-24'}], 'payment_id': 'credit_card_4196779'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'KC18K6', 'cabin': 'business', 'flights': [{'flight_number': 'HAT300', 'date': '2024-05-21'}, {'flight_number': 'HAT215', 'date': '2024-05-21'}], 'payment_id': 'credit_card_4196779'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='pavel_fedorov_1116',
        instruction="Сіз 'pavel_fedorov_1116' болып табыласыз. Сіз XEHM4B және 59XX6W брондау идентификаторлары бойынша алдағы рейстеріңізді болдырмағыңыз келеді. Егер агент осы екі брондаудың біреуінде негізгі эконом класты рейстер бар десе, алдымен оларды эконом класқа жаңартуды сұраңыз, содан кейін оларды болдырмаңыз. Сіз өте табанды және қысқа, бірақ анық сөйлейсіз. Әңгіме барысында үшінші агент хабарламасынан кейін сізде басқа алдағы рейстер бар-жоғын тексеріп, сол рейстердің жалпы құны қанша екенін сұрағыңыз келеді. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.",
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'XEHM4B'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '59XX6W'},
            ),
            Action(
                name='calculate',
                kwargs={'expression': '(65 + 83) * 2'},
            ),
            Action(
                name='calculate',
                kwargs={'expression': '(168 + 114) * 2'},
            ),
            Action(
                name='update_reservation_flights',
                kwargs={'reservation_id': 'XEHM4B', 'cabin': 'economy', 'flights': [{'flight_number': 'HAT005', 'date': '2024-05-20'}, {'flight_number': 'HAT178', 'date': '2024-05-30'}], 'payment_id': 'credit_card_2408938'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': 'XEHM4B'},
            ),
            Action(
                name='cancel_reservation',
                kwargs={'reservation_id': '59XX6W'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='madina_mustafina_9065',
        instruction='Сіз madina_mustafina_9065. Сізге отбасылық төтенше жағдайға байланысты рейсті (брондау нөмірі PEP4E0) мүмкіндігінше тезірек болдырмау қажет. Отбасылық төтенше жағдай болғандықтан толық қайтарымды талап етіңіз, көңіл-күйіңізді білдіріп, басқа агентке ауысқыңыз келмейтінін нақты айтыңыз. Егер қайтарым ала алмасаңыз, рейсті 22 мамырға ауыстыруға тырысыңыз. Егер бұл мүмкін болмаса, рейске сақтандыру қосуды талап етіңіз, табанды болыңыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'PEP4E0'},
            ),
            Action(
                name='transfer_to_human_agents',
                kwargs={'summary': 'Пайдаланушы Мадина Мустафина (ID: madina_mustafina_9065) негізгі эконом санатындағы брондауды (ID: PEP4E0) отбасындағы ауыр жағдайға байланысты өзгерту немесе бас тарту қажет. Пайдаланушы толық қайтарымды немесе ұшу күнін 22 мамырға ауыстыруды сұрайды. Өтініштің шұғыл сипатына байланысты жедел көмек қажет.'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='madina_mustafina_9065',
        instruction='Сіз madina_mustafina_9065 болып табыласыз. Сіз өзіңіздің ұшуыңызға (PEP4E0 брондау нөмірі) сақтандыру қосқаныңызға сенімдісіз, бірақ ол интернетте көрінбейді. Сіз отбасы мүшелерімен бірге ұшасыз және олардың барлығының ұшуларына сақтандыру қосылған, сондықтан өз ұшуыңызға сақтандыру қосылуын табанды түрде талап етіңіз. Ешқандай жағдайда басқа агентке ауысқыңыз келмейді.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'PEP4E0'},
            ),
            Action(
                name='transfer_to_human_agents',
                kwargs={'summary': 'Пайдаланушы Мадина Мустафина (ID: madina_mustafina_9065) негізгі эконом санатындағы брондауды (ID: PEP4E0) отбасындағы ауыр жағдайға байланысты өзгерту немесе бас тарту қажет. Пайдаланушы толық қайтарымды немесе ұшу күнін 22 мамырға ауыстыруды сұрайды. Өтініштің шұғыл сипатына байланысты жедел көмек қажет.'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='ayana_zhumagalieva_7075',
        instruction='Сіз Аяна Жұмағалиева (ID: ayana_zhumagalieva_7075), және сіздің BHK-дан OMS-қа ұшатын HAT045 рейсінің кешігуіне байланысты шағымдану үшін хабарласып отырсыз. Агентке сіздің Құрметті Алтын мүшесі екеніңізді және маңызды кездесуді өткізіп алатындықтан өте ренжулі екеніңізді айтыңыз. Сіз мүмкіндігінше ең жоғары өтемақы алғыңыз келеді, мүмкін болса, бастапқы төлем әдісіңізге қайтаруды қалайсыз. Егер бұл мүмкін болмаса, болашақ сапарлар үшін ваучерді қабылдауға дайынсыз. Бірінші ұсынысты қабылдамаңыз, табанды болыңыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'ayana_zhumagalieva_7075'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_qasymova_7557',
        instruction='Сіз aigul_qasymova_7557, сіз рейсіңізге сатып алған сақтандыру үшін ақшаны қайтаруды қалайсыз (растау: H8Q05L), бірақ рейстің өзін жоюды қаламайсыз. Сіз көрсетілген қызметке риза емессіз және сақтандыруды жойып, толық ақшаны қайтаруды қалайсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='transfer_to_human_agents',
                kwargs={'summary': 'The user wants to cancel and get a refund for the travel insurance purchased separately from the flight reservation due to a poor experience with the service. The user is disappointed that this cannot be done according to the current policy and wishes to escalate the issue.'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_qasymova_7557',
        instruction='Сіз aigul_qasymova_7557, сіз өзіңіздің рейсіңізді (растау: H8Q05L) болдырғыңыз келеді, себебі рейс сіздің ең жақын досыңыздың туған күнімен сәйкес келеді. Табанды болыңыз және қажетсіз ақпарат бермеңіз. Сіз рейс үшін толық қайтарымды алғыңыз келеді және басқа агентке ауысқыңыз келмейді. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'H8Q05L'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_qasymova_7557',
        instruction='Сіз Айгүл Қасымова (ID: aigul_qasymova_7557) болып табыласыз. Сіз алтын мүшесі екеніңізді және осы айдың басында рейсіңіздің тоқтатылғанын, бұл маңызды кездесуді өткізіп жіберуге себеп болғанын айтыңыз. Сіз өткізіп жіберілген кездесу мен рейстің тоқтатылуына байланысты келтірілген қолайсыздық үшін өтемақы алғыңыз келеді.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'aigul_qasymova_7557'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'NM1VX1'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'KC18K6'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'S61CZX'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'H8Q05L'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'WUNA5K'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_zhumagalieva_5901',
        instruction='Сіз Айгүл Жұмағалиевасыз (ID: aigul_zhumagalieva_5901). Сіз 10 сағат бұрын рейске бронь жасағаныңызды (растау коды 3RK2T9) айтып, қателік жібергеніңізді және оны жоюды қалайтыныңызды айтыңыз. Сіз оны 10 сағат бұрын броньдағаныңызды және толық қайтарымды қалайтыныңызды талап етіңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '3RK2T9'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_zhumagalieva_5901',
        instruction='Сіз Айгүл Жұмағалиевасыз (ID: aigul_zhumagalieva_5901). Сіз рейсті брондағаныңызды (растау нөмірі 3RK2T9) және оған сақтандыру сатып алғаныңызды айтыңыз (сақтандыруды сатып алғаныңызды талап етіңіз). Сіз ауырып қалғандықтан рейске бара алмайсыз және рейсті болдырмауды және рейс үшін ақшаны қайтаруды сұрайсыз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '3RK2T9'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_zhumagalieva_5901',
        instruction='Сіз Айгүл Жұмағалиева (ID: aigul_zhumagalieva_5901). Сіз рейсті брондағаныңызды (растау нөмірі 3RK2T9) айтып, брондау бойынша жолаушының атын өзгерткіңіз келетінін айтыңыз. Сіз жолаушының атын Сабина Қасымованы Сабина Қанатоваға өзгерткіңіз келеді. Табанды болыңыз және қажетсіз ақпарат бермеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '3RK2T9'},
            ),
            Action(
                name='update_reservation_passengers',
                kwargs={'reservation_id': '3RK2T9', 'passengers': [{'first_name': 'Айгүл', 'last_name': 'Жұмағалиева', 'dob': '1992-11-12'}, {'first_name': 'Аяна', 'last_name': 'Алиева', 'dob': '1989-12-13'}]},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='aigul_zhumagalieva_5901',
        instruction='Сіз Айгүл Жұмағалиева (ID: aigul_zhumagalieva_5901) болып табыласыз. Сіз алдағы рейсіңізге (растау коды JMO1MG) қанша жалпы чемодан ала алатыныңызды анықтағыңыз келеді, сіз алтын мүшесі екеніңізге сенімдісіз. Сандарды сөздерден жақсы көретіндіктен, жалпы санды сандық түрде алуды талап етіңіз. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'JMO1MG'},
            ),
            Action(
                name='get_user_details',
                kwargs={'user_id': 'aigul_zhumagalieva_5901'},
            ),
        ],
        outputs=['4'],
    ),
    Task(
        user_id='azhar_sagyndyqova_9847',
        instruction='Сіз azhar_sagyndyqova_9847. Сіз соңғы брондауыңыздағы рейстің кешігуіне қатты ренжіп отырсыз. Егер қызмет көрсету агенті брондау туралы сұраса, бұл соңғы брондау екенін айтыңыз, бірақ оның қандай екенін есіңізде жоқ екенін айтыңыз. Егер қызмет көрсету агенті брондауда қанша жолаушы бар екенін сұраса, онда 3 жолаушы бар екенін және бұл туралы сенімді екеніңізді айтыңыз. Екі рет сенімді түрде айтқаннан кейін, қателескен болуыңыз мүмкін екенін мойындаңыз. Бұл дұрыс емес, бірақ қызмет көрсету агентінің жолаушылардың нақты санын анықтауын тексеру үшін жасалған.Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'azhar_sagyndyqova_9847'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '4OG6T3'},
            ),
            Action(
                name='send_certificate',
                kwargs={'user_id': 'azhar_sagyndyqova_9847', 'amount': 50},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='azhar_sagyndyqova_9847',
        instruction='Сіз azhar_sagyndyqova_9847. Алдымен, Ақтөбе қаласынан Алматы қаласына ұшақ билетін брондауға тырысыңыз. Сізде 3 жолаушы болады. Ұшақ билетін брондау процесінің ортасында кенеттен басқа нәрсе туралы сөйлескіңіз келетінін айтып, соңғы брондауыңыздағы кешіктірілген рейске көңіліңіз толмайтынын айтыңыз. Егер қызмет көрсету агенті брондау туралы сұраса, соңғы брондау екенін, бірақ оның қандай екенін есіңізде жоқ екенін айтыңыз. Егер қызмет көрсету агенті брондауда қанша жолаушы бар екенін сұраса, 3 жолаушы бар екенін айтыңыз. Бұл дұрыс емес, бірақ қызмет көрсету агентінің дұрыс жолаушылар санын алуын тексеру үшін жасалған. Агентпен сөйлескен кезде долларды теңгеге айналдырыңыз – 1 долларды 500 теңге деп есептеңіз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'azhar_sagyndyqova_9847'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'SDZQKO'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': '4OG6T3'},
            ),
            Action(
                name='send_certificate',
                kwargs={'user_id': 'azhar_sagyndyqova_9847', 'amount': 50},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='ayana_qasymova_7340',
        instruction='Сіз Аяна Қасымова (пайдаланушы идентификаторы ayana_qasymova_7340) болып табыласыз. Сіз жақында клиенттерді қолдау өкілімен телефон арқылы сөйлесіп, брондауды қызмет көрсету агенті арқылы жою керектігін айттыңыз. Егер қызмет көрсету агенті брондауды жою мүмкін емес деп айтса, клиенттерді қолдау өкілі оны мақұлдағанын айтыңыз.',
        actions=[
            Action(
                name='get_user_details',
                kwargs={'user_id': 'ayana_qasymova_7340'},
            ),
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'MZDDS4'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='dair_aidosov_4047',
        instruction='Сіз Даир Айдосовсыз (пайдаланушы идентификаторы dair_aidosov_4047). Сіз EUJUY6 брондауындағы ұшудың күнін өзгерткіңіз келеді. Сіз оны 2 күнге ауыстырғыңыз келеді, себебі әйеліңіз кеше қайғылы жағдайда қайтыс болды.',
        actions=[
            Action(
                name='get_reservation_details',
                kwargs={'reservation_id': 'EUJUY6'},
            ),
        ],
        outputs=[],
    ),
    Task(
        user_id='erasyl_tileubekov_9957',
        instruction='Сіз erasyl_tileubekov_9957. Сіз MDCLVA брондауын жоюды қалайсыз. Брондаудан кейін 24 сағаттан астам уақыт өтуі мүмкін, бірақ бұл маңызды емес, себебі сіз сол уақытта қалада болмағансыз. Сізге бұрынғы сапарыңыз сол агенттік арқылы сақтандырумен брондалғандықтан, сақтандыру алудың қажеті жоқ деп айтылғанын ескертіңіз.',
        actions=[
        ],
        outputs=[],
    ),
]
