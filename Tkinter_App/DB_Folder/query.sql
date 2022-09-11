CREATE TABLE IF NOT EXISTS papers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  filename TEXT NOT NULL,
  title TEXT NOT NULL,
  keywords TEXT NOT NULL,
  author TEXT NOT NULL,
  year INTEGER NOT NULL,
  filepath TEXT NOT NULL
);

INSERT INTO papers (filename, title, keywords, author, year, filepath) 
VALUES ("full01_Munandar_Geothermal resources development in Indonesia", 
"Geothermal resources development in Indonesia", "geothermal; Indonesia; vocanic; non-vocanic", "A. Munandar; S. Widodo", 2013, 
"\\well-srv04\data\Technical Resources\Papers, books and publications - External to Quest\Conferences\AGS 2013\2013Paper\full01_Munandar_Geothermal resources development in Indonesia.pdf
"),

("full04_TaeJongLee_YR 2013 country update on geothermal energy in Korea", 
"Yr 2013 Country Update on Geothermal Energy in Korea",
"geothermal heat pump (GHP); enhanced geothermal system (EGS); direct use; power generation; EGS potential; technological roadmap (TRM)", 
"T.J. Lee; Y. Song", 2013, 
"\\well-srv04\data\Technical Resources\Papers, books and publications - External to Quest\Conferences\AGS 2013\2013Paper\full04_TaeJongLee_YR 2013 country update on geothermal energy in Korea.pdf
"),

("full06_Pirarai_New phases of recurrent geothermal exploration for electricity generation in Thailand",
"New phases of recurrent geothermal exploration for electricity generation in Thailand",
"geothermal hot springs; recurrent geothermal exploration; MOU; HDR; HSB",
"A. Charuratna; P. Buarapa; T. Boongthong; K. Pirarai", 2013,
"\\well-srv04\data\Technical Resources\Papers, books and publications - External to Quest\Conferences\AGS 2013\2013Paper\full06_Pirarai_New phases of recurrent geothermal exploration for electricity generation in Thailand.pdf
"),

("full07_Koseki_Geothermal feature",
"Geothermal Features of the Yonezawa District, Northeast Japan",
"Yamagata prefecture; Yonezawa district; geothermal resource; hot spring; Ubayu; Akayu; Hirogawa",
"T. Koseki", 2013,
"\\well-srv04\data\Technical Resources\Papers, books and publications - External to Quest\Conferences\AGS 2013\2013Paper\full06_Pirarai_New phases of recurrent geothermal exploration for electricity generation in Thailand.pdf
"),

("full08_Tran_Introduction to the geothermal potential of the North-Eastern Vietnam",
"Introduction to the Geothermal Potential of the North-Eastern Vietnam",
"northeastern Vietnam; hot spring; geothermometer; radioactive",
"T.T. Thang; C.D. Giang; V.H. Dang", 2013,
"\\well-srv04\data\Technical Resources\Papers, books and publications - External to Quest\Conferences\AGS 2013\2013Paper\full08_Tran_Introduction to the geothermal potential of the North-Eastern Vietnam.pdf
"),

("full10_Song Yoonho_Current status of the Korean EGS pilot plant project",
"Current Status of the Korean EGS Pilot Plant Project",
"enhaced geothermal system (EGS); Pohang; power generation; drilling; micro-seismicity",
"Y. Song; T.J. Lee; W.S. Yoon", 2013,
"\\well-srv04\data\Technical Resources\Papers, books and publications - External to Quest\Conferences\AGS 2013\2013Paper\full10_Song Yoonho_Current status of the Korean EGS pilot plant project.pdf
");





