import json

page_tocs = {
    "StartPage": {
        "default": True,
        "menu": [
            {
                'function': "default_page",
                'type': 'button',
                'key': "btn_about_this_programm"
            },
            {
                'type': 'switch_page',
                "target": "NumbersPage",
                'key': "btn_numbers_overview"
            },
            {
                'type': 'language_switcher',
                'key': "btn_change_language"
            },
            {
                'type': 'quit_button',
                "key": "btn_exit"
            },
        ],
        "TOC": {
            "about": {
                "default": True,
                "content": [
                    {"type": "headline", "key": 'btn_about_this_programm'},
                    {"type": "seperator"},
                    {"type": "paragraph", "key": "about_page_paragraph_1"},
                    {"type": "paragraph", "key": "about_page_paragraph_2"},
                ]
            }
        }
    },
    "NumbersPage": {
        "config": {
            "audio_examples_path": "assets/audio/numbers/",
            "audio_examples_filename": "{}_{}.mp3",
            "available_speakers": [
                {"number": "0", "name": "Felix", "gender": "♂"},
                {"number": "1", "name": "Hans", "gender": "♂"},
                {"number": "4", "name": "Emil", "gender": "♂"},
                {"number": "2", "name": "Lara", "gender": "♀"},
                {"number": "3", "name": "Jeanette", "gender": "♀"},
            ]
        },
        "menu": [
            {
                'type': 'switch_page',
                "target": "StartPage",
                'key': "btn_back"
            },
            {
                'type': 'switch_content',
                "target": "numbers_overview",
                'key': "headline_numbers_overview"
            },
            {
                'type': 'switch_content',
                "target": "numbers_1_12",
                'key': "btn_numbers_1_12"
            },
            {
                'type': 'switch_content',
                "target": "numbers_13_19",
                'key': "btn_numbers_13_19"
            },
            {
                'type': 'switch_content',
                "target": "numbers_with_two_digits",
                'key': "btn_numbers_with_two_digits"
            },
            {
                'type': 'switch_content',
                "target": "numbers_20_29",
                'key': "btn_numbers_20_29"
            },
            {
                'type': 'switch_content',
                "target": "numbers_30_39",
                'key': "btn_numbers_30_39"
            },
            {
                'type': 'switch_content',
                "target": "numbers_40_49",
                'key': "btn_numbers_40_49"
            },
            {
                'type': 'switch_content',
                "target": "numbers_50_59",
                'key': "btn_numbers_50_59"
            },
            {
                'type': 'switch_content',
                "target": "numbers_60_69",
                'key': "btn_numbers_60_69"
            },
            {
                'type': 'switch_content',
                "target": "numbers_70_79",
                'key': "btn_numbers_70_79"
            },
            {
                'type': 'switch_content',
                "target": "numbers_80_89",
                'key': "btn_numbers_80_89"
            },
            {
                'type': 'switch_content',
                "target": "numbers_90_99",
                'key': "btn_numbers_90_99"
            },
            {
                'type': 'switch_content',
                "target": "numbers_hundreds",
                'key': "btn_numbers_hundreds"
            },
            {
                'type': 'switch_content',
                "target": "numbers_thousands",
                'key': "btn_numbers_thousands"
            },
            {
                'type': 'switch_content',
                "target": "numbers_millions",
                'key': "btn_numbers_millions"
            },
            {
                'type': 'switch_page',
                "target": "NumberQuizPage",
                'key': "btn_numbers_quiz_page"
            },
        ],
        "TOC": {
            "numbers_overview": {
                "default": True,
                "content": [
                    {"type": "headline", "key": 'headline_numbers_overview'},
                    {"type": "seperator"},
                    {"type": "paragraph", "key": "btn_numbers_overview_paragraph_1"},
                    {"type": "paragraph", "key": "btn_numbers_overview_paragraph_2"},
                    {"type": "paragraph", "key": "btn_numbers_overview_paragraph_3"},
                ]
            },
            "numbers_1_12": {
                "content": [
                    {"key": 'btn_numbers_1_12', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "0 - Null", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["0"]},
                    {"type": "seperator"},
                    {"key": "1 - Eins", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["1"]},
                    {"type": "seperator"},
                    {"key": "2 - Zwei", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["2"]},
                    {"type": "seperator"},
                    {"key": "3 - Drei", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["3"]},
                    {"type": "seperator"},
                    {"key": "4 - Vier", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["4"]},
                    {"type": "seperator"},
                    {"key": "5 - Fünf", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["5"]},
                    {"type": "seperator"},
                    {"key": "6 - Sechs", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["6"]},
                    {"type": "seperator"},
                    {"key": "7 - Sieben", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["7"]},
                    {"type": "seperator"},
                    {"key": "8 - Acht", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["8"]},
                    {"type": "seperator"},
                    {"key": "9 - Neun", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["9"]},
                    {"type": "seperator"},
                    {"key": "10 - Zehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["10"]},
                    {"type": "seperator"},
                    {"key": "11 - Elf", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["11"]},
                    {"type": "seperator"},
                    {"key": "12 - Zwölf", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["12"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_13_19": {
                "content": [
                    {"key": 'btn_numbers_13_19', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "13 - Dreizehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["13"]},
                    {"type": "seperator"},
                    {"key": "14 - Vierzehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["14"]},
                    {"type": "seperator"},
                    {"key": "15 - Fünfzehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["15"]},
                    {"type": "seperator"},
                    {"key": "16 - Sechzehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["16"]},
                    {"type": "seperator"},
                    {"key": "17 - Siebzehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["17"]},
                    {"type": "seperator"},
                    {"key": "18 - Achtzehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["18"]},
                    {"type": "seperator"},
                    {"key": "19 - Neunzehn", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["19"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_with_two_digits": {
                "content": [
                    {"key": 'btn_numbers_with_two_digits', "type": "headline"},
                    {"type": "seperator"},
                    {"key": 'numbers_with_two_digits_paragraph_1', "type": "paragraph"},
                    {"key": 'numbers_with_two_digits_paragraph_2', "type": "paragraph"},
                    {"type": "newline"},
                    {"key": 'numbers_with_two_digits_paragraph_3', "type": "paragraph"},
                    {"key": 'numbers_with_two_digits_paragraph_4', "type": "paragraph"},
                    {"key": 'numbers_with_two_digits_paragraph_5', "type": "paragraph"},
                    {"key": 'numbers_with_two_digits_paragraph_6', "type": "paragraph"},
                    {"type": "newline"},
                    {"key": 'numbers_with_two_digits_paragraph_7', "type": "headline"},
                    {"type": "seperator"},
                    {"key": 'numbers_with_two_digits_paragraph_8', "type": "paragraph"},
                    {"type": "newline"},
                    {"key": 'numbers_with_two_digits_paragraph_9', "type": "paragraph"},
                ]
            },
            "numbers_20_29": {
                "content": [
                    {"key": 'btn_numbers_20_29', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "20 - Zwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["20"]},
                    {"type": "seperator"},
                    {"key": "21 - Einundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["21"]},
                    {"type": "seperator"},
                    {"key": "22 - Zweiundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["22"]},
                    {"type": "seperator"},
                    {"key": "23 - Dreiundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["23"]},
                    {"type": "seperator"},
                    {"key": "24 - Vierundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["24"]},
                    {"type": "seperator"},
                    {"key": "25 - Fünfundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["25"]},
                    {"type": "seperator"},
                    {"key": "26 - Sechsundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["26"]},
                    {"type": "seperator"},
                    {"key": "27 - Siebenundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["27"]},
                    {"type": "seperator"},
                    {"key": "28 - Achtundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["28"]},
                    {"type": "seperator"},
                    {"key": "29 - Neunundzwanzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["29"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_30_39": {
                "content": [
                    {"key": 'btn_numbers_30_39', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "30 - Dreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["30"]},
                    {"type": "seperator"},
                    {"key": "31 - Einunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["31"]},
                    {"type": "seperator"},
                    {"key": "32 - Zweiunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["32"]},
                    {"type": "seperator"},
                    {"key": "33 - Dreiunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["33"]},
                    {"type": "seperator"},
                    {"key": "34 - Vierunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["34"]},
                    {"type": "seperator"},
                    {"key": "35 - Fünfunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["35"]},
                    {"type": "seperator"},
                    {"key": "36 - Sechsunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["36"]},
                    {"type": "seperator"},
                    {"key": "37 - Siebenunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["37"]},
                    {"type": "seperator"},
                    {"key": "38 - Achtunddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["38"]},
                    {"type": "seperator"},
                    {"key": "39 - Neununddreißig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["39"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_40_49": {
                "content": [
                    {"key": 'btn_numbers_40_49', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "40 - Vierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["40"]},
                    {"type": "seperator"},
                    {"key": "41 - Einundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["41"]},
                    {"type": "seperator"},
                    {"key": "42 - Zweiundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["42"]},
                    {"type": "seperator"},
                    {"key": "43 - Dreiundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["43"]},
                    {"type": "seperator"},
                    {"key": "44 - Vierundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["44"]},
                    {"type": "seperator"},
                    {"key": "45 - Fünfundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["45"]},
                    {"type": "seperator"},
                    {"key": "46 - Sechsundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["46"]},
                    {"type": "seperator"},
                    {"key": "47 - Siebenundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["47"]},
                    {"type": "seperator"},
                    {"key": "48 - Achtundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["48"]},
                    {"type": "seperator"},
                    {"key": "49 - Neunundvierzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["49"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_50_59": {
                "content": [
                    {"key": 'btn_numbers_50_59', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "50 - Fünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["50"]},
                    {"type": "seperator"},
                    {"key": "51 - Einundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["51"]},
                    {"type": "seperator"},
                    {"key": "52 - Zweiundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["52"]},
                    {"type": "seperator"},
                    {"key": "53 - Dreiundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["53"]},
                    {"type": "seperator"},
                    {"key": "54 - Vierundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["54"]},
                    {"type": "seperator"},
                    {"key": "55 - Fünfundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["55"]},
                    {"type": "seperator"},
                    {"key": "56 - Sechsundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["56"]},
                    {"type": "seperator"},
                    {"key": "57 - Siebenundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["57"]},
                    {"type": "seperator"},
                    {"key": "58 - Achtundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["58"]},
                    {"type": "seperator"},
                    {"key": "59 - Neunundfünfzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["59"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_60_69": {
                "content": [
                    {"key": 'btn_numbers_60_69', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "60 - Sechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["60"]},
                    {"type": "seperator"},
                    {"key": "61 - Einundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["61"]},
                    {"type": "seperator"},
                    {"key": "62 - Zweiundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["62"]},
                    {"type": "seperator"},
                    {"key": "63 - Dreiundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["63"]},
                    {"type": "seperator"},
                    {"key": "64 - Vierundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["64"]},
                    {"type": "seperator"},
                    {"key": "65 - Fünfundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["65"]},
                    {"type": "seperator"},
                    {"key": "66 - Sechsundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["66"]},
                    {"type": "seperator"},
                    {"key": "67 - Siebenundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["67"]},
                    {"type": "seperator"},
                    {"key": "68 - Achtundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["68"]},
                    {"type": "seperator"},
                    {"key": "69 - Neunundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["69"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_70_79": {
                "content": [
                    {"key": 'btn_numbers_70_79', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "70 - Siebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["70"]},
                    {"type": "seperator"},
                    {"key": "71 - Einundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["71"]},
                    {"type": "seperator"},
                    {"key": "72 - Zweiundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["72"]},
                    {"type": "seperator"},
                    {"key": "73 - Dreiundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["73"]},
                    {"type": "seperator"},
                    {"key": "74 - Vierundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["74"]},
                    {"type": "seperator"},
                    {"key": "75 - Fünfundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["75"]},
                    {"type": "seperator"},
                    {"key": "76 - Sechsundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["76"]},
                    {"type": "seperator"},
                    {"key": "77 - Siebenundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["77"]},
                    {"type": "seperator"},
                    {"key": "78 - Achtundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["78"]},
                    {"type": "seperator"},
                    {"key": "79 - Neunundsiebzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["79"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_80_89": {
                "content": [
                    {"key": 'btn_numbers_80_89', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "80 - Achtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["80"]},
                    {"type": "seperator"},
                    {"key": "81 - Einundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["81"]},
                    {"type": "seperator"},
                    {"key": "82 - Zweiundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["82"]},
                    {"type": "seperator"},
                    {"key": "83 - Dreiundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["83"]},
                    {"type": "seperator"},
                    {"key": "84 - Vierundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["84"]},
                    {"type": "seperator"},
                    {"key": "85 - Fünfundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["85"]},
                    {"type": "seperator"},
                    {"key": "86 - Sechsundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["86"]},
                    {"type": "seperator"},
                    {"key": "87 - Siebenundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["87"]},
                    {"type": "seperator"},
                    {"key": "88 - Achtundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["88"]},
                    {"type": "seperator"},
                    {"key": "89 - Neunundachtzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["89"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_90_99": {
                "content": [
                    {"key": 'btn_numbers_90_99', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "90 - Neunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["90"]},
                    {"type": "seperator"},
                    {"key": "91 - Einundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["91"]},
                    {"type": "seperator"},
                    {"key": "92 - Zweiundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["92"]},
                    {"type": "seperator"},
                    {"key": "93 - Dreiundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["93"]},
                    {"type": "seperator"},
                    {"key": "94 - Vierundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["94"]},
                    {"type": "seperator"},
                    {"key": "95 - Fünfundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["95"]},
                    {"type": "seperator"},
                    {"key": "96 - Sechsundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["96"]},
                    {"type": "seperator"},
                    {"key": "97 - Siebenundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["97"]},
                    {"type": "seperator"},
                    {"key": "98 - Achtundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["98"]},
                    {"type": "seperator"},
                    {"key": "99 - Neunundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["99"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_hundreds": {
                "content": [
                    {"key": 'btn_numbers_hundreds', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "numbers_hundreds_paragraph_1", "type": "paragraph"},
                    {"key": "numbers_hundreds_paragraph_2", "type": "paragraph"},
                    {"key": "numbers_hundreds_paragraph_3", "type": "paragraph"},
                    {"type": "seperator"},
                    {"key": "100 - Einhundert (Hundert)", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["100"]},
                    {"type": "seperator"},
                    {"key": "200 - Zweihundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["200"]},
                    {"type": "seperator"},
                    {"key": "300 - Dreihundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["300"]},
                    {"type": "seperator"},
                    {"key": "400 - Vierhundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["400"]},
                    {"type": "seperator"},
                    {"key": "500 - Fünfhundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["500"]},
                    {"type": "seperator"},
                    {"key": "600 - Sechshundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["600"]},
                    {"type": "seperator"},
                    {"key": "700 - Siebenhundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["700"]},
                    {"type": "seperator"},
                    {"key": "800 - Achthundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["800"]},
                    {"type": "seperator"},
                    {"key": "900 - Neunhundert", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["900"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_thousands": {
                "content": [
                    {"key": 'btn_numbers_thousands', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "numbers_thousands_paragraph_1", "type": "paragraph"},
                    {"key": "numbers_thousands_paragraph_2", "type": "paragraph"},
                    {"type": "seperator"},
                    {"key": "1.000 - Eintausend (Tausend)", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["1", "tausend"]},
                    {"type": "seperator"},
                    {"key": "2.000 - Viertausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["2", "tausend"]},
                    {"type": "seperator"},
                    {"key": "3.000 - Dreitausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["3", "tausend"]},
                    {"type": "seperator"},
                    {"key": "4.000 - Viertausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["4", "tausend"]},
                    {"type": "seperator"},
                    {"key": "5.000 - Fünftausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["5", "tausend"]},
                    {"type": "seperator"},
                    {"key": "6.000 - Sechstausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["6", "tausend"]},
                    {"type": "seperator"},
                    {"key": "7.000 - Siebentausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["7", "tausend"]},
                    {"type": "seperator"},
                    {"key": "8.000 - Achttausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["8", "tausend"]},
                    {"type": "seperator"},
                    {"key": "9.000 - Neuntausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["9", "tausend"]},
                    {"type": "seperator"},
                    {"key": "10.000 - Zehntausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["10", "tausend"]},
                    {"type": "seperator"},
                    {"key": "11.000 - Elftausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["11", "tausend"]},
                    {"type": "seperator"},
                    {"key": "12.000 - Zwölftausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["12", "tausend"]},
                    {"type": "seperator"},
                    {"key": "13.000 - Dreizehntausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["13", "tausend"]},
                    {"type": "seperator"},
                    {"key": "23.000 - Dreiundzwanzigtausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["23", "tausend"]},
                    {"type": "seperator"},
                    {"key": "33.000 - Dreiunddreißigtausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["33", "tausend"]},
                    {"type": "seperator"},
                    {"key": "100.000 - Einhunderttausend (Hunderttausend)", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["100", "tausend"]},
                    {"type": "seperator"},
                    {"key": "200.000 - Zweihunderttausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["200", "tausend"]},
                    {"type": "seperator"},
                    {"key": "666.666 - Sechshundertsechsundsechzigtausendsechshundertsechsundsechzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["600", "66", "tausend", "600", "66"]},
                    {"type": "seperator"},
                    {"key": "700.000 - Siebenhunderttausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["700", "tausend"]},
                    {"type": "seperator"},
                    {"key": "999.000 - Neunhundertneunundneunzigtausend", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["900", "99", "tausend"]},
                    {"type": "seperator"},
                ]
            },
            "numbers_millions": {
                "content": [
                    {"key": 'btn_numbers_millions', "type": "headline"},
                    {"type": "seperator"},
                    {"key": "1.000.000 - Eine million", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["eine", "million"]},
                    {"type": "seperator"},
                    {"key": "2.000.000 - Zwei millionen", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["2", "millionen"]},
                    {"type": "seperator"},
                    {"key": "3.000.000 - Drei millionen", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["3", "millionen"]},
                    {"type": "seperator"},
                    {"key": "10.000.000 - Zehn millionen", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["10", "millionen"]},
                    {"type": "seperator"},
                    {"key": "100.000.000 - Einhundert millionen (Hundert millionen)", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["100", "millionen"]},
                    {"type": "seperator"},
                    {"key": "105.000.000 - Einhundertfünf millionen", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["100", "5", "millionen"]},
                    {"type": "seperator"},
                    {"key": "277.000.000 - Zweihundertsiebenundsiebzig millionen", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["200", "77", "millionen"]},
                    {"type": "seperator"},
                    {"key": "999.999.999 - Neunhundertneunundneunzig millionen Neunhundertneunundneunzigtausendneunhundertneunundneunzig", "type": "paragraph"},
                    {"type": "audio_examples", "data": ["900", "99", "millionen", "900", "99", "tausend", "900", "99"]},
                    {"type": "seperator"},
                ]
            },
        }
    },
    "NumberQuizPage": {
        "menu": [
            {
                'type': 'switch_page',
                "target": "NumbersPage",
                'key': "btn_back"
            },
            {
                'type': 'switch_content',
                "target": "quiz",
                'key': "quiz"
            },
        ],
        "TOC": {
            "about": {
                "default": True,
                "content": [
                    {"type": "headline", "key": 'headline_numbers_quiz_page'},
                    {"type": "seperator"},
                ]
            },
            "quiz": {
                "type": "quiz",
                "content": [
                    {"type": "headline", "key": 'i am a headline for quizzes'},
                    {"type": "seperator"},
                ]
            }
        }
    },
}


def save_toc_as_json():

    with open("TOC.json", "w") as f:
        f.write(json.dumps(get_toc(), indent=4, sort_keys=False))


def get_toc():
    return page_tocs


if __name__ == "__main__":
    pass
    #save_toc_as_json()
