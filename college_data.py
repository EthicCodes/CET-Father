# college_data.py

DTE_CODE_TO_COLLEGE = {
    "01002": "Government College of Engineering, Amravati",
    "01005": "Sant Gadge Baba Amravati University, Amravati",
    "01012": "Government College of Engineering, Yavatmal",
    "01101": "Shri Sant Gajanan Maharaj College of Engineering, Shegaon",
    "01105": "Prof. Ram Meghe Institute of Technology & Research, Amravati",
    "01107": "P. R. Pote Patil College of Engineering & Management, Amravati",
    "01114": "Sipna Shikshan Prasarak Mandal College of Engineering & Technology, Amravati",
    "01116": "Shri Shivaji Education Society's College of Engineering and Technology, Akola",
    "01117": "Janata Shikshan Prasarak Mandal’s Babasaheb Naik College Of Engineering, Pusad",
    "01119": "Paramhansa Ramkrishna Maunibaba Shikshan Santha's, Anuradha Engineering College, Chikhali",
    "01120": "Jawaharlal Darda Institute of Engineering and Technology, Yavatmal",
    "01121": "Shri Hanuman Vyayam Prasarak Mandals College of Engineering & Technology, Amravati",
    "01123": "Dr.Rajendra Gode Institute of Technology & Research, Amravati",
    "01125": "Dwarka Bahu Uddeshiya Gramin Vikas Foundation, Rajarshi Shahu College of Engineering, Buldhana",
    "01126": "Takshashila Institute of Engineering & Technology, Darapur, Amravati",
    "01127": "Jagadambha Bahuuddeshiya Gramin Vikas Sanstha's Jagdambha College of Engineering and Technology, Yavatmal",
    "01128": "Prof Ram Meghe College of Engineering and Management, Badnera",
    "01130": "Vision Buldhana Educational & Welfare Society's Pankaj Laddhad Institute of Technology & Management Studies, Yelgaon",
    "01180": "Sanmati Engineering College, Sawargaon Barde, Washim",
    "01182": "Padmashri Dr. V.B. Kolte College of Engineering, Malkapur, Buldhana",
    "01265": "Mauli Group of Institutions, College of Engineering and Technology, Shegaon",
    "01268": "Siddhivinayak Technical Campus, School of Engineering & Research Technology, Shirasgon, Nile",
    "01276": "Manav School of Engineering & Technology, Gut No. 1035 Nagpur Surat Highway, NH No. 6 Tal.Vyala, Balapur, Akola, 444302",
    "02008": "Government College of Engineering, Chhatrapati Sambhajinagar",
    "02020": "Shri Guru Gobind Singhji Institute of Engineering and Technology, Nanded",
    "02021": "University Department of Chemical Technology, Aurangabad",
    "02032": "Institute of Chemical Technology, Mumbai Marathwada off campus, Jalna",
    "02111": "Everest Education Society, Group of Institutions (Integrated Campus), Ohar",
    "02112": "Shree Yash Pratishthan, Shreeyash College of Engineering and Technology, Aurangabad",
    "02113": "G. S. Mandal's Maharashtra Institute of Technology, Aurangabad",
    "02114": "Deogiri Institute of Engineering and Management Studies, Aurangabad",
    "02116": "Matoshri Pratishan's Group of Institutions (Integrated Campus), Kupsarwadi, Nanded",
    "02127": "Mahatma Gandhi Missions College of Engineering, Hingoli Rd, Nanded",
    "02129": "M.S. Bidve Engineering College, Latur",
    "02130": "Terna Public Charitable Trust's College of Engineering, Osmanabad",
    "02131": "Shree Tuljabhavani College of Engineering, Tuljapur",
    "02133": "Mahatma Basaweshwar Education Society's College of Engineering, Ambejogai",
    "02134": "Peoples Education Society's College of Engineering, Aurangabad",
    "02135": "Hi-Tech Institute of Technology, Aurangabad",
    "02136": "Aditya Engineering College, Beed",
    "02137": "Nagnathappa Halge Engineering College, Parli, Beed",
    "02138": "Matsyodari Shikshan Sansatha's College of Engineering and Technology, Jalna",
    "02146": "Adarsh Shikshan Prasarak Mandal's K. T. Patil College of Engineering and Technology, Osmanabad",
    "02250": "Aurangabad College of Engineering, Naygaon Savangi, Aurangabad",
    "02252": "Marathwada Shikshan Prasarak Mandal's Shri Shivaji Institute of Engineering and Management Studies, Parbhani",
    "02254": "Vilasrao Deshmukh Foundation Group of Institutions, Latur",
    "02282": "Aditya Education Trust's Mitthulalji Sarada Polytechnic, Nalwandi Road, Beed",
    "02508": "Gramin Technical and Management Campus, Nanded",
    "02516": "International Centre Of Excellence In Engineering and Management (ICEEM)",
    "02522": "STMEI's Sandipani Technical Campus-Faculty of Engineering, Latur",
    "02533": "CSMSS Chh. Shahu College of Engineering, Aurangabad",
    "02637": "Jijau Institute of Engineering Technology and Management, Khandgaon (Bendri), Taluka Naigaon, District Nanded",
    "02641": "Dr. V.K. Patil College of Engineering & Technology",
    "02666": "Mangaldeep College of Engineering",
    "02758": "Sant Eknath College of Engineering",
    "03012": "Veermata Jijabai Technological Institute (VJTI), Matunga, Mumbai",
    "03014": "Sardar Patel College of Engineering, Andheri",
    "03025": "SVKM's Shri Bhagubhai Mafatlal Polytechnic & College of Engineering",
    "03033": "Dr. Babasaheb Ambedkar Technological University, Lonere",
    "03035": "Usha Mittal Institute of Technology SNDT Women's University, Mumbai",
    "03036": "Institute of Chemical Technology, Matunga, Mumbai",
    "03042": "Loknete Shamrao Peje Government College of Engineering, Ratnagiri",
    "03135": "Manjara Charitable Trust's Rajiv Gandhi Institute of Technology, Mumbai",
    "03139": "Vidyalankar Institute of Technology, Wadala, Mumbai",
    "03143": "Thakur Shyamnarayan Engineering College, Mumbai",
    "03146": "Jawahar Education Society's Annasaheb Chudaman Patil College of Engineering, Kharghar, Navi Mumbai",
    "03147": "Saraswati Education Society, Yadavrao Tasgaonkar Institute of Engineering & Technology, Karjat",
    "03148": "Mahavir Education Trust's Shah & Anchor Kutchhi Engineering College, Mumbai",
    "03154": "Saraswati Education Society's Saraswati College of Engineering, Kharghar Navi Mumbai",
    "03175": "M.G.M.'s College of Engineering and Technology, Kamothe, Navi Mumbai",
    "03176": "Thakur College of Engineering and Technology, Kandivali, Mumbai",
    "03182": "Thadomal Shahani Engineering College, Bandra, Mumbai",
    "03183": "Anjuman-I-Islam's M.H. Saboo Siddik College of Engineering, Byculla, Mumbai",
    "03184": "Fr. Conceicao Rodrigues College of Engineering, Bandra, Mumbai",
    "03185": "Vivekanand Education Society's Institute of Technology, Chembur, Mumbai",
    "03187": "N.Y.S.S.'s Datta Meghe College of Engineering, Airoli, Navi Mumbai",
    "03188": "Vasantdada Patil Pratishthan's College Of Engineering and Visual Arts, Sion, Mumbai",
    "03189": "Bharati Vidyapeeth College of Engineering, Navi Mumbai",
    "03190": "Terna Engineering College, Nerul, Navi Mumbai",
    "03192": "Smt. Indira Gandhi College of Engineering, Navi Mumbai",
    "03193": "Shivajirao S. Jondhale College of Engineering, Dombivali, Mumbai",
    "03194": "Vidyavardhini's College of Engineering and Technology, Vasai",
    "03196": "Lokmanya Tilak College of Engineering, Kopar Khairane, Navi Mumbai",
    "03197": "Agnel Charities' FR. C. Rodrigues Institute of Technology, Vashi, Navi Mumbai",
    "03198": "Konkan Gyanpeeth College of Engineering, Karjat",
    "03199": "Shri Vile Parle Kelvani Mandal's Dwarkadas J. Sanghvi College of Engineering, Vile Parle, Mumbai",
    "03200": "Hope Foundation and research center's Finolex Academy of Management and Technology, Ratnagiri",
    "03201": "Rizvi Education Society's Rizvi College of Engineering, Bandra, Mumbai",
    "03202": "Rajendra Mane College of Engineering & Technology Ambav Deorukh",
    "03203": "Atharva College of Engineering, Malad(West), Mumbai",
    "03204": "St. Francis Institute of Technology, Borivali, Mumbai",
    "03206": "S.S.P.M.'s College of Engineering, Kankavli",
    "03207": "Mahatma Education Society's Pillai College of Engineering, New Panvel",
    "03208": "Don Bosco Institute of Technology, Mumbai",
    "03209": "K J Somaiya Institute of Technology",
    "03210": "Excelsior Education Society's K.C. College of Engineering and Management Studies and Research, Kopri, Thane (E)",
    "03211": "S.I.E.S. Graduate School of Technology, Nerul, Navi Mumbai",
    "03212": "Watumull Institute of Engineering & Technology, Ulhasnagar",
    "03214": "Xavier Institute Of Engineering C/O Xavier Technical Institute, Mahim, Mumbai",
    "03215": "Bhartiya Vidya Bhavan's Sardar Patel Institute of Technology, Andheri, Mumbai",
    "03216": "Gharda Foundation's Gharda Institute of Technology, Khed, Ratnagiri",
    "03217": "Vighnaharata Trust's Shivajirao S. Jondhale College of Engineering & Technology, Shahapur, Asangaon, Dist Thane",
    "03218": "Aldel Education Trust's St. John College of Engineering & Management, Vevoor, Palghar",
    "03219": "Koti Vidya Charitable Trust's Smt. Alamuri Ratnamala Institute of Engineering and Technology, Sapgaon, Tal. Shahapur",
    "03220": "Yadavrao Tasgaonkar College of Engineering & Management",
    "03221": "Vishnu Waman Thakur Charitable Trust's VIVA Institute of Technology, Virar",
    "03222": "Haji Jamaluddin Thim Trust's Theem College of Engineering, At. Villege Betegaon, Boisar",
    "03223": "Mahatma Education Society's Pillai HOC College of Engineering & Technology, Tal. Khalapur. Dist. Raigad",
    "03224": "Leela Education Society, G.V. Acharya Institute of Engineering and Technology, Shelu, Karjat",
    "03257": "Vidya Prasarak Mandal's College of Engineering, Thane",
    "03277": "Pravin Rohidas Patil College of Engineering & Technology",
    "03351": "Bharat College of Engineering, Kanhor, Badlapur(W)",
    "03353": "Dilkap Research Institute Of Engineering and Management Studies, At.Mamdapur, Post- Neral, Tal- Karjat, Mumbai",
    "03423": "Shree L.R. Tiwari College of Engineering, Mira Road, Mumbai",
    "03436": "B.R. Harne College of Engineering & Technology, Karav, Tal-Ambernath",
    "03439": "Anjuman-I-Islam's Kalsekar Technical Campus, Panvel",
    "03440": "Metropolitan Institute of Technology & Management, Sukhalwad, Sindhudurg",
    "03445": "Vishwatmak Jangli Maharaj Ashram Trust (Kokamthan), Atma Malik Institute Of Technology & Research",
    "03447": "G.M.Vedak Institute of Technology, Tala, Raigad",
    "03460": "Universal College of Engineering, Kaman Dist. Palghar",
    "03462": "VPM's Maharshi Parshuram College of Engineering, Velneshwar, Ratnagiri",
    "03465": "Ideal Institute of Technology, Wada, Dist.Thane",
    "03467": "Vishwaniketan's Institute of Management Entrepreneurship and Engineering Technology(i MEET), Khalapur Dist Raigad",
    "03470": "Yashwantrao Bhonsale Institute of Technology",
    "03471": "New Horizon Institute of Technology & Management, Thane",
    "03475": "A. P. Shah Institute of Technology, Thane",
    "03477": "Chhartrapati Shivaji Maharaj Institute of Technology, Shedung, Panvel",
    "03503": "Indala College Of Engineering, Bapsai Tal.Kalyan",
    "03546": "Devi Mahalaxmi College of Engineering and Technology",
    "04004": "Government College of Engineering, Chandrapur",
    "04025": "Government College of Engineering, Nagpur",
    "04104": "Kavi Kulguru Institute of Technology & Science, Ramtek",
    "04116": "Ankush Shikshan Sanstha's G.H.Raisoni College of Engineering, Nagpur",
    "04118": "Bapurao Deshmukh College of Engineering, Sevagram",
    "04123": "Lokmanya Tilak Jankalyan Shikshan Sanstha, Priyadarshani College of Engineering, Nagpur",
    "04133": "Sanmarg Shikshan Sanstha's Smt. Radhikatai Pandav College of Engineering, Nagpur",
    "04134": "Guru Nanak Institute of Engineering & Technology, Kalmeshwar, Nagpur",
    "04135": "Amar Seva Mandal's Shree Govindrao Vanjari College of Engineering & Technology, Nagpur",
    "04136": "Lokmanya Tilak Jankalyan Shikshan Sastha, Priyadarshini J. L. College Of Engineering, Nagpur",
    "04137": "Sir Shantilal Badjate Charitable Trust's S. B. Jain Institute of technology, Management & Research, Nagpur",
    "04138": "Jaidev Education Society, J D College of Engineering and Management, Nagpur",
    "04139": "Samridhi Sarwajanik Charitable Trust, Jhulelal Institute of Technology, Nagpur",
    "04141": "Shriram Gram Vikas Shikshan Sanstha, Vilasrao Deshmukh College of Engineering and Technology, Nagpur",
    "04142": "G H Raisoni College of Engineering & Management, Nagpur",
    "04143": "Sanmarg Shikshan Sanstha, Mandukarrao Pandav College of Engineering, Bhandara",
    "04144": "Shri. Sai Shikshan Sanstha, Nagpur Institute of Technology, Nagpur",
    "04145": "Wainganga College of Engineering and Management, Dongargaon, Nagpur",
    "04147": "K.D.K. College of Engineering, Nagpur",
    "04151": "Tulsiramji Gaikwad Patil College of Engineering & Technology, Nagpur",
    "04163": "Rajiv Gandhi College of Engineering Research & Technology, Chandrapur",
    "04167": "Yeshwantrao Chavan College of Engineering, Wanadongri, Nagpur",
    "04172": "Anjuman College of Engineering & Technology, Nagpur",
    "04174": "St. Vincent Pallotti College of Engineering & Technology, Nagpur",
    "04175": "JMSS Shri Shankarprasad Agnihotri College of Engineering, Wardha",
    "04177": "Priyadarshini Bhagwati College of Engineering, Harpur Nagar, Umred Road, Nagpur",
    "04181": "Swaminarayan Siddhanta Institute Of Technology, Nagpur",
    "04188": "Krushi Jivan Vikas Pratishthan, Ballarpur Institute of Technology, Mouza Bamni",
    "04190": "M.D. Yergude Memorial Shikshan Prasarak Mandal's Shri Sai College of Engineering & Technology, Bhadrawati",
    "04192": "Maitraya Education Society, Nagarjuna Institute of Engineering Technology & Management, Nagpur",
    "04193": "K.D.M. Education Society, Vidharbha Institute of Technology, Umred Road, Nagpur",
    "04196": "Gurunanak Educational Society's Gurunanak Institute of Technology, Nagpur",
    "04197": "Jai Mahakali Shikshan Sanstha, Agnihotri College of Engineering, Sindhi(Meghe)",
    "04285": "V M Institute of Engineering and Technology, Dongargaon, Nagpur",
    "04302": "Gondia Education Society's Manoharbhai Patel Institute Of Engineering & Technology, Shahapur, Bhandara",
    "04304": "Cummins College of Engineering For Women, Sukhali (Gupchup), Tal. Hingna Hingna Nagpur",
    "04613": "Suryodaya College of Engineering & Technology, Nagpur",
    "04648": "R.V. Parankar College of Engineering & Technology, Arvi, Dist Wardha",
    "04649": "Bajaj Institute of Technology, Wardha",
    "04679": "Karanjekar College of Engineering & Management, Sakoli",
    "04703": "Somayya Institute of Technology, Chandrapur",
    "05003": "University Institute of Chemical Technology, North Maharashtra University, Jalgaon",
    "05004": "Government College of Engineering, Jalgaon",
    "05103": "Shri Shivaji Vidya Prasarak Sanstha's Late Bapusaheb Shivaji Rao Deore College of Engineering, Dhule",
    "05104": "Shramsadhana Bombay Trust, College of Engineering & Technology, Jalgaon",
    "05106": "Khandesh College Education Society's College Of Engineering And Management, Jalgaon",
    "05108": "Maratha Vidya Prasarak Samaj's Karmaveer Adv. Baburao Ganpatrao Thakare College Of Engineering, Nashik",
    "05109": "Sandip Foundation, Sandip Institute of Technology and Research Centre, Mahiravani, Nashik",
    "05121": "K. K. Wagh Institute of Engineering Education and Research, Nashik",
    "05124": "Jagadamba Education Soc. Nashik's S.N.D. College of Engineering & Research, Babulgaon",
    "05125": "Pravara Rural Education Society's Sir Visvesvaraya Institute of Technology, Chincholi Dist. Nashik",
    "05130": "Brahma Valley College of Engineering & Research, Trimbakeshwar, Nashik",
    "05139": "Pravara Rural College of Engineering, Loni, Pravaranagar, Ahmednagar",
    "05151": "MET Bhujbal Knowledge City MET League's Engineering College, Adgaon, Nashik",
    "05152": "G H Raisoni College of Engineering and Management, Jalgaon",
    "05160": "Sanjivani Rural Education Society's Sanjivani College of Engineering, Kopargaon",
    "05161": "Dr. Vithalrao Vikhe Patil College of Engineering, Ahmednagar",
    "05162": "Amrutvahini Sheti & Shikshan Vikas Sanstha's Amrutvahini College of Engineering, Sangamner",
    "05164": "P.S.G.V.P. Mandal's D.N. Patel College of Engineering, Shahada, Dist. Nandurbar",
    "05168": "T.M.E. Society's J.T.Mahajan College of Engineering, Faizpur",
    "05169": "Nagaon Education Society's Gangamai College of Engineering, Nagaon, Tal Dist Dhule",
    "05170": "Hindi Seva Mandal's Shri Sant Gadgebaba College of Engineering & Technology, Bhusawal",
    "05171": "Godavari Foundation's Godavari College Of Engineering, Jalgaon",
    "05172": "R. C. Patel Institute of Technology, Shirpur",
    "05173": "SNJB's Late Sau. Kantabai Bhavarlalji Jain College of Engineering, (Jain Gurukul), Neminagar, Chandwad, Nashik",
    "05177": "Matoshri College of Engineering and Research Centre, Eklahare, Nashik",
    "05179": "Vishwabharati Academy's College of Engineering, Ahmednagar",
    "05181": "Gokhale Education Society's, R.H. Sapat College of Engineering, Management Studies and Research, Nashik",
    "05182": "Kalyani Charitable Trust, Late Gambhirrao Natuba Sapkal College of Engineering, Anjaneri, Trimbakeshwar Road, Nashik",
    "05184": "Amruta Vaishnavi Education & Welfare Trust's Shatabdi Institute of Engineering & Research, Agaskhind Tal. Sinnar",
    "05244": "MET's Institute of Technology Polytechnic, Bhujbal Knowledge City, Adgaon Nashik",
    "05256": "Matoshri Education Society, Matoshri Asarabai Polytechnic, Nashik",
    "05263": "Matoshri Education Society, Matoshri Institute Of Technology, Dhanore, Nashik",
    "05303": "Hon. Shri. Babanrao Pachpute Vichardhara Trust, Group of Institutions (Integrated Campus)-Parikrama, Kashti Shrigondha",
    "05322": "Jamia Institute Of Engineering And Management Studies, Akkalkuwa",
    "05330": "Pune Vidyarthi Griha’s College of Engineering & Shrikrishna S. Dhamankar Institute of Management, Nashik",
    "05331": "Sandip Foundation's, Sandip Institute of Engineering & Management, Nashik",
    "05365": "Vardhaman Education & Welfare Society, Ahinsa Institute of Technology, Post. Dondaicha, Dhule",
    "05370": "Kedareshwar Gramin Vikas Pratishthan, Samajbhushan Eknathrao Dhakane College, of Engineering, Shevgaon",
    "05380": "Adsul's Technical Campus, Chas Dist. Ahmednagar",
    "05381": "Shri. Jaykumar Rawal Institute of Technology, Dondaicha",
    "05382": "Ahmednagar Jilha Maratha Vidya Prasarak Samajache, Shri. Chhatrapati Shivaji Maharaj College of Engineering, Nepti",
    "05390": "K.V.N. Naik S. P. Sansth's Loknete Gopinathji Munde Institute of Engineering Education & Research, Nashik",
    "05396": "College of Engineering and Technology, North Maharashtra Knowledge City, Jalgaon",
    "05399": "Sanghavi College of Engineering, Varvandi, Nashik",
    "05401": "Jawahar Education Society's Institute of Technology, Management & Research, Nashik",
    "05408": "Vidya Niketan College of Engineering, Bota Sangamner",
    "05409": "Rajiv Gandhi College of Engineering, At Post Karjule Hariya Tal.Parner, Dist.Ahmednagar",
    "05411": "Maulana Mukhtar Ahmad Nadvi Technical Campus, Malegaon",
    "05418": "Guru Gobind Singh College of Engineering & Research Centre, Nashik",
    "05433": "R.C. Patel College of Engineering and Polytechnic, Shirpur",
    "05449": "Shri Vile Parle Kelavani Mandal's Institute of Technology, Dhule",
    "05497": "P.G. College of Engineering & Technology, Nandurbar",
    "05509": "Shri Swami Samarth Institute of Management and Technology, Malwadi-Bota",
    "05513": "MKD Institute of Technology, Nadurbar",
    "05545": "Shri. Vile Parle Kelwani Mandal's College of Engineering, Shirpur",
    "06004": "Government College of Engineering & Research, Avasari Khurd",
    "06005": "Government College of Engineering, Karad",
    "06007": "Walchand College of Engineering, Sangli",
    "06028": "Department of Technology, Shivaji University, Kolhapur",
    "06036": "Government College of Engineering, Kolhapur",
    "06122": "TSSMS's Pd. Vasantdada Patil Institute of Technology, Bavdhan, Pune",
    "06138": "Genba Sopanrao Moze Trust Parvatibai Genba Moze College of Engineering, Wagholi, Pune",
    "06139": "Progressive Education Society's Modern College of Engineering, Pune",
    "06141": "Jaywant Shikshan Prasarak Mandal's, Rajarshi Shahu College of Engineering, Tathawade, Pune",
    "06144": "Genba Sopanrao Moze College of Engineering, Baner-Balewadi, Pune",
    "06145": "JSPM'S Jaywantrao Sawant College of Engineering, Pune",
    "06146": "MIT Academy of Engineering, Alandi, Pune",
    "06149": "Siddhant College of Engineering, A/p Sudumbare, Tal.Maval, Dist-Pune",
    "06155": "G.H.Raisoni College of Engineering & Management, Wagholi, Pune",
    "06156": "Marathwada Mitra Mandal's College of Engineering, Karvenagar, Pune",
    "06175": "Pimpri Chinchwad Education Trust, Pimpri Chinchwad College of Engineering, Pune",
    "06177": "Sinhgad College of Engineering, Vadgaon (BK), Pune",
    "06178": "Sinhgad Technical Education Society's Smt. Kashibai Navale College of Engineering, Vadgaon, Pune",
    "06179": "Indira College of Engineering & Management, Pune",
    "06182": "Sinhgad Technical Education Society, Sinhgad Institute of Technology and Science, Narhe (Ambegaon)",
    "06183": "Al-Ameen Educational and Medical Foundation, College of Engineering, Koregaon, Bhima",
    "06184": "K. J.'s Educational Institute Trinity College of Engineering and Research, Pisoli, Haveli",
    "06185": "Sinhgad Institute of Technology",
    "06187": "Sinhgad Academy of Engineering, Kondhwa (BK) Kondhwa-Saswad Road, Pune",
    "06203": "Marathwada Mitra Mandal's Institute of Technology, Lohgaon, Pune",
    "06206": "Pune District Education Association's College of Engineering, Manjari(Bk), Hadapsar, Pune",
    "06207": "Dr. D. Y. Patil Unitech Society's Dr. D. Y. Patil Institute of Technology, Pimpri, Pune",
    "06214": "K. E. Society's Rajarambapu Institute of Technology, Walwa, Sangli",
    "06217": "Shri. Balasaheb Mane Shikshan Prasarak Mandal's, Ashokrao Mane Group of Institutions",
    "06219": "KSGBS's Bharat- Ratna Indira Gandhi College of Engineering, Kegaon, Solapur",
    "06220": "Shri Vithal Education and Research Institute's College of Engineering, Pandharpur",
    "06222": "Dattajirao Kadam Technical Education Society's Textile & Engineering Institute, Ichalkaranji",
    "06223": "Pradnya Niketan Education Society's Nagesh Karajagi Orchid College of Engineering & Technology, Solapur",
    "06250": "D.Y. Patil College of Engineering and Technology, Kolhapur",
    "06265": "Walchand Institute of Technology, Solapur",
    "06267": "Kolhapur Institute of Technology's College of Engineering (Autonomous), Kolhapur",
    "06268": "Tatyasaheb Kore Institute of Engineering and Technology, Warananagar",
    "06269": "Shetkari Shikshan Mandal's Pad. Vasantraodada Patil Institute of Technology, Budhgaon, Sangli",
    "06270": "Rayat Shikshan Sanstha's Karmaveer Bhaurao Patil College of Engineering, Satara",
    "06271": "Pune Institute of Computer Technology",
    "06272": "Dr. D. Y. Patil Pratishthan's D.Y.Patil College of Engineering Akurdi, Pune",
    "06273": "Bansilal Ramnath Agarawal Charitable Trust's Vishwakarma Institute of Technology, Bibwewadi, Pune",
    "06274": "Pune Vidyarthi Griha's College of Engineering and Technology and G K Pate(Wani) Institute of Management, Pune",
    "06275": "Shivnagar Vidya Prasarak Mandal's College of Engineering, Malegaon-Baramati",
    "06276": "MKSSS's Cummins College of Engineering for Women, Karvenagar, Pune",
    "06277": "Dr. J. J. Magdum Charitable Trust's Dr. J.J. Magdum College of Engineering, Jaysingpur",
    "06278": "All India Shri Shivaji Memorial Society's College of Engineering, Pune",
    "06281": "Modern Education Society's Wadia College of Engineering, Pune",
    "06282": "All India Shri Shivaji Memorial Society's Institute of Information Technology, Pune",
    "06283": "Annasaheb Dange College of Engineering and Technology, Ashta, Sangli",
    "06284": "Vidya Pratishthan's Kamalnayan Bajaj Institute of Engineering & Technology, Baramati Dist.Pune",
    "06285": "Bharati Vidyapeeth's College of Engineering for Women, Katraj, Dhankawadi, Pune",
    "06288": "Bharati Vidyapeeth's College of Engineering, Kolhapur",
    "06293": "Kai Amdar Bramhadevdada Mane Shikshan & Samajik Prathistan's Bramhadevdada Mane Institute of Technology, Solapur",
    "06298": "Zeal Education Society's Zeal College of Engineering & Research, Narhe, Pune",
    "06303": "Dr. Ashok Gujar Technical Institute's Dr. Daulatrao Aher College of Engineering, Karad",
    "06304": "Loknete Hanumantrao Charitable Trust's Adarsh Institute of Technology and Research Centre, Vita, Sangli",
    "06305": "Late Narayandas Bhawandas Chhabada Institute of Engineering & Technology, Satara",
    "06307": "Dhole Patil Education Society, Dhole Patil College of Engineering, Wagholi, Tal. Haveli",
    "06308": "Shanti Education Society, A.G. Patil Institute of Technology, Soregaon, Solapur(North)",
    "06310": "Nutan Maharashtra Vidya Prasarak Mandal, Nutan Maharashtra Institute of Engineering & Technology, Talegaon station, Pune",
    "06311": "Jayawant Shikshan Prasarak Mandal, Bhivarabai Sawant Institute of Technology & Research, Wagholi",
    "06313": "Jaywant College of Engineering & Polytechnic, Kille Macchindragad Tal. Walva District- Sangali",
    "06315": "Sanjeevan Group of Institutions",
    "06317": "Sharad Institute of Technology College of Engineering, Yadrav(Ichalkaranji)",
    "06318": "Abhinav Education Society's College of Engineering and Technology (Degree), Wadwadi",
    "06319": "Shahajirao Patil Vikas Pratishthan, S.B.Patil College of Engineering, Vangali, Tal. Indapur",
    "06320": "K.J.'s Educational Institute's K.J. College of Engineering & Management Research, Pisoli",
    "06321": "Vidya Vikas Pratishthan Institute of Engineering and Technology, Solapur",
    "06322": "Shree Gajanan Maharaj Shikshan Prasarak Mandal's Sharadchandra Pawar College of Engineering, Dumbarwadi",
    "06324": "Rajgad Dnyanpeeth's Shri Chhatrapati Shivajiraje College of Engineering, Bhor",
    "06325": "Alard Charitable Trust's Alard College of Engineering and Management, Pune",
    "06326": "Karmayogi Institute of Technology",
    "06402": "New Institute of Technology, Kolhapur",
    "06444": "Shriram Institute Of Engineering & Technology, (Poly), Paniv",
    "06466": "Shree Santkrupa Shikshan Sanstha, Shree Santkrupa Institute Of Engineering & Technology, Karad",
    "06468": "Swami Vivekananda Shikshan Sanstha, Dr. Bapuji Salunkhe Institute Of Engineering & Technology, Kolhapur",
    "06545": "Samarth Education Trust's Arvind Gavali College Of Engineering Panwalewadi, Varye, Satara",
    "06609": "Jaihind College Of Engineering, Kuran",
    "06622": "ISBM College Of Engineering, Pune",
    "06625": "Universal College of Engineering & Research, Sasewadi",
    "06628": "Dattakala Group Of Institutions, Swami - Chincholi Tal. Daund Dist. Pune",
    "06632": "Navsahyadri Education Society's Group of Institutions",
    "06634": "KJEI's Trinity Academy of Engineering, Yewalewadi, Pune",
    "06635": "Samarth College of Engineering and Management",
    "06640": "N. B. Navale Sinhgad College of Engineering, Kegaon, Solapur",
    "06643": "S K N Sinhgad College of Engineering, Korti Tal. Pandharpur Dist Solapur",
    "06644": "Shri. Ambabai Talim Sanstha's Sanjay Bhokare Group of Institutes, Miraj",
    "06649": "TSSM's Bhivarabai Sawant College of Engineering and Research, Narhe, Pune",
    "06714": "Appasaheb Alias Sa.Re.Patil Institute of Technology, Dattanagar Tal-Shirol, Dist Kolhapur",
    "06732": "Ajeenkya DY Patil School of Engineering, Lohegaon, Pune",
    "06754": "International Institute of Information Technology (I²IT), Pune",
    "06755": "JSPM Narhe Technical Campus, Pune",
    "06756": "Fabtech Technical Campus College of Engineering and Research, Sangola",
    "06757": "Yashoda Technical Campus, Wadhe, Satara",
    "06758": "Sahyadri Valley College of Engineering & Technology, Rajuri, Pune",
    "06759": "Shree Ramchandra College of Engineering, Lonikand, Pune",
    "06762": "Nanasaheb Mahadik College of Engineering, Walwa, Sangli",
    "06766": "Phaltan Education Society's College of Engineering Thakurki Tal- Phaltan Dist-Satara",
    "06767": "Suman Ramesh Tulsiani Technical Campus: Faculty of Engineering, Kamshet, Pune",
    "06768": "P.K. Technical Campus, Pune",
    "06769": "Rasiklal M. Dhariwal Sinhgad Technical Institutes Campus, Warje, Pune",
    "06770": "SKN Sinhgad Institute of Technology & Science, Kusgaon(BK), Pune",
    "06771": "Flora Institute of Technology, Khopi, Near Khed Shivapur Toll Plaza, Pune",
    "06772": "NBN Sinhgad Technical Institutes Campus, Pune",
    "06780": "D.Y.Patil Education Society's, D.Y.Patil Technical Campus, Faculty of Engineering & Faculty of Management, Talsande, Kolhapur",
    "06781": "Bhagwant Institute of Technology, Barshi",
    "06782": "Sahakar Maharshee Shankarrao Mohite Patil Institute of Technology & Research, Akluj",
    "06794": "Anantrao Pawar College of Engineering & Research, Pune",
    "06795": "Shri.Someshwar Shikshan Prasarak Mandal, Sharadchandra Pawar College of Engineering & Technology, Someshwar Nagar",
    "06796": "Bharati Vidyapeeth's College of Engineering, Lavale, Pune",
    "06797": "Dnyanshree Institute Engineering and Technology, Satara",
    "06799": "Shivganga Charitable Trust, Sangli Vishveshwarya Technical Campus, Faculty of Diploma Engineering, Patgaon, Miraj",
    "06803": "Sant Gajanan Maharaj College of Engineering, Gadhinglaj",
    "06808": "Keystone School of Engineering, Pune",
    "06811": "Sanjay Ghodawat Institute",
    "06815": "Vidya Prasarini Sabha's College of Engineering & Technology, Lonavala",
    "06822": "Pimpri Chinchwad Education Trust's Pimpri Chinchwad College Of Engineering And Research, Ravet",
    "06834": "Dr.D.Y.Patil College Of Engineering & Innovation, Talegaon",
    "06839": "Dr. D Y Patil Pratishthan's College of Engineering, Kolhapur",
    "06878": "Dr. A. D. Shinde College Of Engineering, Tal.Gadhinglaj, Kolhapur",
    "06901": "MAEER's MIT College of Railway Engineering and Research, Jamgaon, Barshi",
    "06938": "Shree Siddheshwar Women's College Of Engineering, Solapur",
    "06991": "Dr. D.Y. Patil Technical Campus, Varale, Talegaon, Pune",
    "14005": "Laxminarayan Innovation Technological University, Nagpur",
    "16006": "COEP Technological University",
    "16121": "Shri. Anandrao Abitkar College of Engineering, Pal",
    "16126": "Tatyasaheb Kore Institute of Engineering and Technology, Yelur"
}
