import math

# list of (most) Belgian communities, with coordinates according to a Mercator projection.

all_communes = [("Aalst", (575061.8368696974, 5644396.819551783)),("Aalter", (531519.6775850406, 5659184.536941301)),\
    ("Aarschot", (629867.1340910662, 5649141.00455739)),("Aartselaar", (596785.2232017588, 5665558.287847248)),\
    ("Affligem", (578131.916279454, 5639292.55774853)),("Aiseau-Presles", (611605.8849598696, 5585675.111576218)),\
    ("Alken", (661843.2732558982, 5637521.925917723)),("Alveringem", (476862.9305763073, 5647819.327231347)),\
    ("Amay", (664097.4560020705, 5603092.769621753)),("Amel", (299755.9311196781, 5581179.214980542)),\
    ("Andenne", (644734.2696348976, 5593989.501413442)),("Anderlues", (590023.892719608, 5583872.888351512)),\
    ("Anhe", (629493.8010256662, 5575681.781995778)),("Ans", (676932.3917471502, 5616676.558691478)),\
    ("Anthisnes", (677323.0513960029, 5596288.086637169)),("Antoing", (532072.291310141, 5600994.955481907)),\
    ("Antwerpen", (598402.8611820805, 5676101.216481376)),("Anzegem", (532281.4096925877, 5630153.242983773)),\
    ("Ardooie", (514036.4175286617, 5648920.934418766)),("Arendonk", (645179.9298505498, 5687104.841836656)),\
    ("Arlon", (702949.0689676828, 5507843.73426384)),("As", (681780.3783705572, 5654878.808651122)),\
    ("Asse", (587494.714443134, 5640064.803612583)),("Assenede", (549164.9474222251, 5676004.830060654)),\
    ("Assesse", (640173.7958752951, 5582317.4966983)),("Ath", (555769.3727866752, 5609444.554041498)),\
    ("Attert", (699049.9862551214, 5514499.956618054)),("Aubange", (700897.7112872971, 5495556.65362417)),\
    ("Aubel", (701253.8662066085, 5620339.42234924)),("Avelgem", (531499.409292546, 5624343.642605989)),\
    ("Awans", (672815.1340988019, 5618208.3775111195)),("Aywaille", (690048.5824210028, 5591344.503075858)),\
    ("Baarle-Hertog", (634336.7707006035, 5701641.316052879)),("Baelen", (711001.3238793609, 5612372.899426975)),\
    ("Balen", (650923.5386815503, 5669643.207425253)),("Bassenge", (683747.6304687974, 5626807.335503256)),\
    ("Bastogne", (698504.4300246993, 5542307.812266889)),("Beaumont", (588414.1961032428, 5564849.882932853)),\
    ("Beauraing", (640561.8766461493, 5551966.283523847)),("Beauvechain", (625031.3637245515, 5627071.289479568)),\
    ("Beernem", (524088.37460205704, 5666562.052657782)),("Beerse", (627204.3060492724, 5685691.397241246)),\
    ("Beersel", (591235.6156755413, 5622821.996712359)),("Begijnendijk", (624546.9133697317, 5651324.3794404175)),\
    ("Bekkevoort", (638957.9695601108, 5644892.966952939)),("Beloeil", (547266.194343384, 5596294.590909748)),\
    ("Beringen", (655341.836385013, 5658645.8628020575)),("Berlaar", (615465.0926880378, 5665020.016304674)),\
    ("Berlare", (567783.7151788385, 5653972.605949475)),("Berloz", (656142.7477354323, 5618796.605941307)),\
    ("Bernissart", (548019.1234657142, 5591475.246051632)),("Bertem", (614178.9978324665, 5635020.9936694065)),\
    ("Bertogne", (690087.6110544755, 5548191.014793346)),("Bertrix", (659858.8752178072, 5523212.332916846)),\
    ("Bever", (565886.7132731619, 5618737.000518143)),("Beveren", (586381.5039238732, 5677430.884342091)),\
    ("Beyne-Heusay", (688579.1125223895, 5612441.613662198)),("Bierbeek", (624674.6592677225, 5633715.691225235)),\
    ("Bilzen", (679103.387621502, 5637231.273660911)),("Binche", (582468.4933755959, 5585173.122729763)),\
    ("Bivre", (645042.3675948129, 5530213.568357716)),("Blankenberge", (509291.4819074223, 5684118.358504216)),\
    ("Blgny", (691421.0156039827, 5617587.589070661)),("Bllingen", (308099.73612143425, 5585968.197248454)),\
    ("Bocholt", (678669.4674333232, 5671467.687867203)),("Boechout", (605435.5841435927, 5670367.129015006)),\
    ("Bonheiden", (608721.0774374988, 5652825.255802491)),("Boom", (595727.0648659591, 5659976.623374548)),\
    ("Boortmeerbeek", (609362.0062963071, 5650057.65018391)),("Borgloon", (654343.2930466533, 5631584.907205405)),\
    ("Bornem", (585786.8385571868, 5660736.027065492)),("Borsbeek", (603631.9869478019, 5673111.564068204)),\
    ("Bouillon", (648540.4855334563, 5521130.600548336)),("Boussu", (557405.83397533, 5587120.945896721)),\
    ("Boutersem", (629689.3787945709, 5632903.757218269)),("Braine-l'Alleud", (596188.7024545703, 5613645.511268306)),\
    ("Braine-le-Château", (590658.7894013869, 5615393.148742575)),("Brainele-Comte", (580769.850903564, 5607823.913876711)),\
    ("Braives", (651941.9981734868, 5609637.202595802)),("Brakel", (553890.482520268, 5628374.78809048)),\
    ("Brasschaat", (601122.7225563, 5682328.164113723)),("Brecht", (613781.5781332657, 5688156.579542413)),\
    ("Bredene", (497675.0900516651, 5675769.777378075)),("Bree", (683303.5366259549, 5667912.703034328)),\
    ("Brugelette", (560867.0500831797, 5605330.944867574)),("Brugge", (515122.8015118689, 5678015.723574741)),\
    ("Brunehaut", (527694.7154880846, 5596978.067339566)),("Bruxelles", (595258.9473207939, 5633171.618740119)),\
    ("Buggenhout", (584172.010676265, 5652367.214284415)),("Burdinne", (648665.6983155829, 5605593.128505874)),\
    ("Burg-Reuland", (294048.4548562814, 5565344.3216604125)),("Bütgenbach", (301780.7995305157, 5591467.23424305)),\
    ("Celles", (531579.824712061, 5616871.3462060345)),("Cerfontaine", (602903.2495787116, 5561240.018858898)),\
    ("Chapellelez-Herlaimont", (591086.298526102, 5590686.683480363)),("Charleroi", (600956.4721202843, 5586172.64945825)),\
    ("Chastre", (615362.1231075837, 5606246.083889803)),("Chaudfontaine", (685811.0643855992, 5607244.52182669)),\
    ("Chaumont-Gistoux", (620311.0661388248, 5616736.495054316)),("Chimay", (595144.8675569103, 5543445.563025068)),\
    ("Chiny", (672789.9336615091, 5510191.407980923)),("Chivres", (554053.6862834, 5602287.149398353)),\
    ("Chtelet", (607392.6186321692, 5584197.36415437)),("Ciney", (650724.4194534793, 5570602.068903068)),\
    ("Clavier", (665752.99750791, 5587865.104012638)),("Colfontaine", (560409.6845956324, 5583451.34907973)),\
    ("Comblainau-Pont", (683230.7068042691, 5596490.411132057)),("Comines-Warneton", (495103.52318248036, 5621404.12495742)),\
    ("Courcelles", (594632.2949556744, 5590904.849775673)),("Court-Saint-Etienne", (610757.0344808369, 5612075.840884769)),\
    ("Couvin", (605277.0089367046, 5544035.663703171)),("Crisne", (669689.7651182405, 5619964.62871628)),\
    ("Dalhem", (693669.8936227434, 5622368.350324328)),("Damme", (522099.0723219638, 5678597.100416728)),\
    ("Daverdisse", (648402.599403578, 5540685.494606131)),("Deerlijk", (524638.431444251, 5633202.8967568865)),\
    ("Deinze", (536376.0073852404, 5647928.79047127)),("Denderleeuw", (573467.9884619622, 5637367.078029815)),\
    ("Dendermonde", (585479.2622560468, 5653078.287198443)),("Dentergem", (528978.6177533733, 5643878.678918511)),\
    ("Dessel", (647774.6611721998, 5677897.996385208)),("Destelbergen", (556084.966003043, 5654766.580090398)),\
    ("Diepenbeek", (668758.7255509131, 5641448.246119825)),("Diest", (644441.0427094006, 5651218.651129325)),\
    ("Diksmuide", (489050.06991409225, 5654818.444039709)),("Dilbeek", (586420.0409890204, 5634485.442998564)),\
    ("Dilsen-Stokkem", (692329.0406077048, 5657487.394747042)),("Dinant", (638054.7314744372, 5568054.557990755)),\
    ("Dison", (702791.5812082024, 5611124.519746604)),("Doische", (624531.6520625395, 5557319.324376361)),\
    ("Donceel", (664656.7232371778, 5613493.446258073)),("Dour", (554503.9349402019, 5581997.110756492)),\
    ("Drogenbos", (592820.3855586345, 5626553.859006321)),("Duffel", (606194.6872294778, 5662039.3454363365)),\
    ("Durbuy", (677020.0588286367, 5581809.125411562)),("Ecaussinnes", (583025.2576007034, 5601675.351396653)),\
    ("Edegem", (601415.2062204207, 5667505.166162011)),("Eeklo", (539608.0881370623, 5670361.483708648)),\
    ("Egheze", (633676.2000113822, 5605890.845053802)),("Ellezelles", (550595.9245441692, 5618566.570298595)),\
    ("Enghien", (573773.3134330143, 5615750.577099098)),("Engis", (669946.4009347766, 5604847.99843085)),\
    ("Ereze", (681931.075283149, 5574184.67630122)),("Erpe-Mere", (566597.5180538503, 5642045.662246838)),\
    ("Erquelinnes", (580717.5432850742, 5572289.823379285)),("Esneux", (682417.0875236314, 5602951.348299222)),\
    ("Essen", (601879.3619115442, 5702745.915906691)),("Estaimpuis", (519680.0097063436, 5615178.381811032)),\
    ("Estinnes", (577161.0890501651, 5581200.493990627)),("Etalle", (688175.8208302902, 5505763.231293022)),\
    ("Eupen", (290840.7279036965, 5614158.480727189)),("Evergem", (553798.2016067408, 5662260.40545239)),\
    ("Faimes", (659284.4475450987, 5612403.580932435)),("Farciennes", (608912.9449663576, 5587009.294154876)),\
    ("Fauvillers", (693979.0191471647, 5528540.231821085)),("Fernelmont", (640149.6229933912, 5601653.778815579)),\
    ("Ferrires", (684745.9311594844, 5587082.183072758)),("Fexhele-Haut-Clocher", (670086.701498782, 5615147.285653853)),\
    ("Fleurus", (608769.5048825373, 5593958.409726663)),("Flobecq", (551749.5114053463, 5620423.913925438)),\
    ("Floreffe", (624559.1556286248, 5589213.10414545)),("Florennes", (614898.8024019552, 5569182.793639975)),\
    ("Florenville", (663103.350436813, 5507732.17113085)),("Flron", (689232.6262669268, 5610617.306578295)),\
    ("Flémalle", (672452.4180395242, 5608391.048994235)),("Fontaine-l'Evêque", (593245.9936691032, 5585786.168476355)),\
    ("Fosses-la-Ville", (617469.5422753621, 5584100.3345110845)),("Frameries", (563031.182303677, 5582369.912355088)),\
    ("Frasnes-lez-Anvaing", (541138.8234145055, 5613657.319546482)),("Froidchapelle", (595175.0632774752, 5560606.851281275)),\
    ("Galmaarden", (570545.2979782928, 5622501.299224071)),("Gavere", (547628.8850727318, 5642626.375732645)),\
    ("Gedinne", (637275.4828894879, 5539765.870932394)),("Geel", (639829.6757872202, 5670264.246580642)),\
    ("Geer", (654118.9127277832, 5615286.8968392005)),("Geetbets", (650472.5587106401, 5638415.33038656)),\
    ("Gembloux", (619956.9484087066, 5600686.798250971)),("Genappe", (602602.6442043544, 5607037.750217719)),\
    ("Gent", (551378.716929099, 5657753.7642620085)),("Geraardsbergen", (563599.4327918029, 5625659.455747057)),\
    ("Gerpinnes", (607897.6166789862, 5578957.555946371)),("Gesves", (645627.8085580608, 5587338.252660731)),\
    ("Gingelom", (652670.3767240081, 5622744.522277437)),("Gistel", (495628.5561229104, 5666507.527398598)),\
    ("Glabbeek", (636325.5591111679, 5637245.854916971)),("Gooik", (575606.885783106, 5638332.029654809)),\
    ("Gouvy", (707833.3016936611, 5564549.1555833295)),("Grez-Doiceau", (618729.7516626893, 5624120.490215036)),\
    ("Grimbergen", (596315.7731555168, 5643769.38440039)),("Grobbendonk", (620561.1225398812, 5671623.113884862)),\
    ("Grâce-Hollogne", (672998.8488219616, 5612649.502479294)),("Haacht", (616116.031287739, 5646311.097047937)),\
    ("Haaltert", (569465.4586711627, 5637312.008070053)),("Habay", (688134.0490627604, 5511326.495354714)),\
    ("Halen", (645930.9239248368, 5646942.943433727)),("Halle", (587044.2064294467, 5620281.217096569)),\
    ("Ham", (650532.6750864442, 5663143.846825773)),("Hamme", (579967.9865157198, 5659708.176624703)),\
    ("Hamoir", (681358.1798802475, 5590860.343879413)),("Hamois", (652690.9129659816, 5577100.717184338)),\
    ("Hamont-Achel", (675632.9407432268, 5680635.55521253)),("Hamsur-Heure-Nalinnes", (599187.591397288, 5575139.004661832)),\
    ("Hannut", (646886.2180760476, 5615234.620042801)),("Harelbeke", (520717.04750128, 5635042.88067543)),\
    ("Hasselt", (661257.4106921463, 5643680.355313859)),("Hastire", (630679.7989544332, 5562205.570784297)),\
    ("Havelange", (660956.8466473597, 5581229.095568007)),("Hechtel-Eksel", (665554.0573070719, 5668245.902769707)),\
    ("Heers", (661748.4102236159, 5624920.992014314)),("Heist-op-den-Berg", (621417.5682309899, 5659905.631403393)),\
    ("Hemiksem", (594421.3388667082, 5667372.0501069)),("Hensies", (550602.1445315466, 5587051.334809108)),\
    ("Herbeumont", (673587.923917996, 5529078.834648557)),("Herent", (615631.5104937332, 5639992.477972061)),\
    ("Herentals", (627445.7678721641, 5668084.2097233)),("Herenthout", (623564.3296585461, 5667989.506502143)),\
    ("Herkde-Stad", (654343.4497727915, 5645083.546790637)),("Herne", (573332.8529916155, 5619447.889877899)),\
    ("Herselt", (631617.8849888365, 5657062.71039092)),("Herstal", (683354.7259816278, 5618289.184183757)),\
    ("Herstappe", (670539.1747786789, 5622952.80009033)),("Herve", (697671.9457321914, 5613712.105976255)),\
    ("Herzele", (562300.0456347585, 5635830.941249488)),("Heusden-Zolder", (660046.1824458783, 5655083.584586394)),\
    ("Heuvelland", (486236.4079353861, 5624689.246294199)),("Hoegaarden", (632775.82663356, 5626806.672780571)),\
    ("Hoeilaart", (603430.7657179404, 5624907.092665287)),("Hoeselt", (673199.4832512584, 5634916.343083581)),\
    ("Holsbeek", (626482.0228456814, 5643950.4254615465)),("Honnelles", (550874.853014897, 5578636.050499062)),\
    ("Hooglede", (506435.69956913724, 5648905.899845577)),("Hoogstraten", (623291.7539327231, 5698390.947717136)),\
    ("Horebeke", (549294.270512512, 5631520.9532919135)),("Hotton", (673725.9688484607, 5570659.762074075)),\
    ("Houffalize", (696618.7325211151, 5559202.536731647)),("Houthalen-Helchteren", (665911.6440039754, 5657127.346085985)),\
    ("Houthulst", (493274.14126947784, 5647049.16847348)),("Houyet", (642904.6129900876, 5560928.897388747)),\
    ("Hove", (602546.1415746133, 5669385.347741382)),("Huldenberg", (613479.2730069435, 5627708.038786954)),\
    ("Hulshout", (626897.4419791532, 5658802.562969844)),("Huy", (657916.2801060772, 5599064.163269633)),\
    ("Hélécine", (640320.1066384572, 5623288.019552621)),("Héron", (648486.2325708166, 5601415.422578638)),\
    ("Ichtegem", (501168.4713619011, 5664648.654808451)),("Ieper", (490187.7985555473, 5633654.198985755)),\
    ("Incourt", (626398.8997224491, 5618359.768094527)),("Ingelmunster", (517573.7807461091, 5640591.441185444)),\
    ("Ittre", (588775.3081761944, 5611034.227933759)),("Izegem", (514055.6830744319, 5641815.071160927)),\
    ("Jabbeke", (506758.6289847475, 5670213.306339272)),("Jalhay", (710086.9837966508, 5605844.695497357)),\
    ("Jemeppesur-Sambre", (618417.6160547894, 5592542.372935019)),("Jodoigne", (631419.6159859067, 5620152.4620154435)),\
    ("Juprelle", (678977.6753526515, 5621387.653067116)),("Jurbise", (564581.5457646517, 5597401.625899075)),\
    ("Kalmthout", (602065.0102806471, 5693471.5167519385)),("Kampenhout", (610089.4466387959, 5643576.385879221)),\
    ("Kapelle-op-den-Bos", (594715.7392690954, 5651314.944222026)),("Kapellen", (599885.5939336196, 5686019.4407556215)),\
    ("Kaprijke", (543079.3658133486, 5673169.7574076)),("Kasterlee", (633405.9706102469, 5678127.182596707)),\
    ("Keerbergen", (613440.0742352771, 5651068.823871083)),("Kelmis", (289797.7987908125, 5622551.350153652)),\
    ("Kinrooi", (694684.5864087363, 5669444.183989937)),("Kluisbergen", (536662.9533355681, 5625122.449846295)),\
    ("Knesselare", (531485.686916595, 5664744.793318172)),("Knokke-Heist", (518865.4488840598, 5686924.979815226)),\
    ("Koekelare", (496105.5604566223, 5659089.699945285)),("Koksijde", (476372.96366323996, 5661922.532501658)),\
    ("Kontich", (601488.1858834994, 5663802.246324789)),("Kortemark", (498828.90338778414, 5653072.179815734)),\
    ("Kortenaken", (642061.4534504376, 5639903.13506983)),("Kortenberg", (610197.5573559416, 5638483.719830634)),\
    ("Kortessem", (668707.2118912262, 5635881.6232333165)),("Kortrijk", (517472.0578317375, 5626913.245592278)),\
    ("Kraainem", (603210.0847629698, 5636026.387924759)),("Kruibeke", (591316.0419187627, 5667315.995407467)),\
    ("Kruishoutem", (536729.9000726787, 5637600.14306513)),("Kuurne", (519943.05899383087, 5633182.77291943)),\
    ("Laakdal", (640490.6440211965, 5660389.967366804)),("Laarne", (561935.9193207101, 5653899.195803429)),\
    ("Lanaken", (686402.0034413248, 5640193.093851063)),("Landen", (645426.8523819272, 5624974.5098703895)),\
    ("Langemark-Poelkapelle", (493751.496686039, 5641177.055830736)),("Lasne", (603231.0445538289, 5615014.368030329)),\
    ("Lebbeke", (577194.8691445489, 5649778.012849682)),("Lede", (566010.8348049696, 5646164.33831381)),\
    ("Ledegem", (509775.6271073809, 5634388.059220368)),("Lendelede", (516411.5901009134, 5636873.461980912)),\
    ("Lennik", (581625.2553590132, 5628223.942133352)),("Lens", (564437.7051997294, 5602771.264647184)),\
    ("Leopoldsburg", (656307.9682141383, 5665174.374306611)),("Lessines", (558254.351973297, 5617478.633886754)),\
    ("Leuven", (620252.6221699617, 5639730.359671957)),("Leuzeen-Hainaut", (543874.9125268409, 5605895.305722033)),\
    ("Libin", (659781.1986137594, 5538631.612723279)),("Libramont-Chevigny", (673986.2909692297, 5535201.12370312)),\
    ("Lichtervelde", (510517.90133398847, 5653538.689779506)),("Liedekerke", (576231.4095451114, 5635560.626154502)),\
    ("Lier", (610817.6196246792, 5663994.527763695)),("Lierde", (559018.9035794655, 5627918.794198638)),\
    ("Lierneux", (698611.4363553608, 5575707.3695129035)),("Lille", (626786.256510421, 5679194.2581191)),\
    ("Limbourg", (707922.8810722512, 5610702.118779529)),("Lincent", (643132.0005708666, 5620894.230150138)),\
    ("Linkebeek", (572842.6760788106, 5626236.398248254)),("Lint", (604949.9819014557, 5665718.277347997)),\
    ("Linter", (644111.6943400082, 5631436.208842693)),("Liège", (683579.5333379293, 5612887.319732314)),\
    ("Lo-Reninge", (483904.17611447425, 5645679.766702762)),("Lobbes", (586853.1412929716, 5578258.96438943)),\
    ("Lochristi", (560966.2276924499, 5661773.0140532525)),("Lokeren", (568422.4731017557, 5664491.457261725)),\
    ("Lommel", (660570.091523024, 5678282.716522124)),("Londerzeel", (589257.4978610621, 5651217.853217238)),\
    ("Lontzen", (289846.08892551996, 5618830.370594834)),("Lovendegem", (543188.0616406573, 5660203.221597067)),\
    ("Lubbeek", (628091.9075711771, 5637970.883363393)),("Lummen", (650911.4734277694, 5650168.17939759)),\
    ("Léglise", (683699.4656635493, 5519520.842196201)),("Maarkedal", (544336.0960748789, 5628240.223955535)),\
    ("Maaseik", (690273.2281854246, 5662599.191323202)),("Maasmechelen", (690567.7930803143, 5647558.3461184)),\
    ("Machelen", (600770.0600817077, 5640605.935858181)),("Maldegem", (531425.1917463407, 5674631.046484351)),\
    ("Malle", (619092.2268901845, 5684572.638371403)),("Malmedy", (288482.38027090044, 5589812.795836139)),\
    ("Manage", (581060.2543748773, 5596328.48985308)),("Manhay", (689273.8012381868, 5574041.0401513865)),\
    ("Marche-en-Famenne", (665505.6545203428, 5563174.955935482)),("Marchin", (659116.0340622868, 5591989.573843859)),\
    ("Martelange", (696551.6478192641, 5523680.383352617)),("Mechelen", (602057.3025901793, 5654847.44805804)),\
    ("Meerhout", (621866.4824208503, 5690201.058113109)),("Meeuwen-Gruitrode", (679453.4308893755, 5664437.442786168)),\
    ("Meise", (592506.3791236567, 5644167.179408817)),("Meixdevant-Virton", (678723.7097750008, 5496729.869394221)),\
    ("Melle", (556145.3167616662, 5649206.487679063)),("Menen", (510571.8861025045, 5626972.520003075)),\
    ("Merbesle-Château", (583047.9062830599, 5575417.542426008)),("Merchtem", (588605.5869886379, 5643787.5842804285)),\
    ("Merelbeke", (551878.997573053, 5646993.307725127)),("Merksplas", (629945.3531481936, 5692258.42656719)),\
    ("Mesen", (492947.9100775329, 5623886.3353621885)),("Messancy", (703192.6404377494, 5500183.443514214)),\
    ("Mettet", (619720.8456136193, 5574784.504357052)),("Meulebeke", (519900.38865284616, 5644302.931547866)),\
    ("Middelkerke", (487697.99573670217, 5666931.842595608)),("Modave", (663770.5915527737, 5594457.973846281)),\
    ("Moerbeke-Waas", (565537.1640349191, 5669581.239796088)),("Mol", (646767.7803977168, 5672304.946141773)),\
    ("Momignies", (586482.5567861935, 5540918.70578983)),("Mons", (567999.4176768633, 5587991.891071947)),\
    ("Mont-Saint-Guibert", (615117.0443803641, 5610312.132481882)),("Mont-de-l'Enclus", (535279.1522978353, 5621220.784688957)),\
    ("Montignyle-Tilleul", (596567.5701269492, 5582130.997867571)),("Moorslede", (505277.78483669134, 5635004.2746407855)),\
    ("Morlanwelz", (587573.3026769285, 5588469.51421182)),("Mortsel", (602546.1415746133, 5669385.347741382)),\
    ("Mouscron", (517058.5148667439, 5619739.462662121)),("Musson", (692815.7334522129, 5493872.772805318)),\
    ("Namur", (632749.6391841022, 5592639.188943688)),("Nandrin", (669828.6076405094, 5599279.558297606)),\
    ("Nassogne", (667013.3491086832, 5557235.176959645)),("Nazareth", (543895.1196840529, 5645373.658479492)),\
    ("Neerpelt", (670778.2794374174, 5677688.7017169455)),("Neufchteau", (673757.227131455, 5523831.831146091)),\
    ("Neupr", (675503.5898364796, 5601235.541340808)),("Nevele", (538547.012235695, 5656151.744804083)),\
    ("Niel", (593320.4614867512, 5663647.787870116)),("Nieuwerkerken", (654470.4755462841, 5638688.506464049)),\
    ("Nieuwpoort", (483674.4555490357, 5664062.764837557)),("Nijlen", (615416.7086195158, 5667177.23021523)),\
    ("Ninove", (570434.6155306741, 5630685.347833621)),("Nivelles", (593409.858818819, 5606543.428272497)),\
    ("Ohey", (653874.0951306722, 5589052.123002628)),("Olen", (629389.9742652907, 5668132.748193168)),\
    ("Olne", (694675.2530108847, 5607098.4420825485)),("Onhaye", (628800.7815949296, 5569312.764097595)),\
    ("Oostende", (495340.40303655533, 5672690.90358615)),("Oosterzele", (555609.2529760983, 5644874.478856179)),\
    ("Oostkamp", (516042.4847692909, 5662827.477491807)),("Oostrozebeke", (523429.3526996354, 5640614.577971368)),\
    ("Opglabbeek", (681061.4143015638, 5658560.437030261)),("Opwijk", (582521.9725864943, 5645844.95490476)),\
    ("Oreye", (666101.1064822093, 5621696.749716994)),("Ottignies-Louvain-la-Neuve", (610698.2323782309, 5614855.570471285)),\
    ("Oud-Heverlee", (619024.3616132681, 5631914.574827314)),("Oud-Turnhout", (638211.8040521299, 5686911.727999432)),\
    ("Oudenaarde", (543326.1043924286, 5633591.89871651)),("Oudenburg", (501167.41865583137, 5669285.975264754)),\
    ("Ouffet", (673929.9990983447, 5591533.858477721)),("Oupeye", (686718.4106158824, 5621914.733235733)),\
    ("Overijse", (609654.2585609037, 5627192.301697896)),("Overpelt", (668776.9920840384, 5676698.601219714)),\
    ("Paliseul", (653932.5059404832, 5530405.1671198)),("Pecq", (524019.6822904305, 5614662.749943586)),\
    ("Peer", (671349.5217758643, 5669359.552116656)),("Pepingen", (581131.6689377583, 5622343.715819955)),\
    ("Pepinster", (698546.4527441575, 5606319.494060245)),("Perwez", (626802.3637622644, 5611327.283070632)),\
    ("Philippeville", (613537.731625762, 5559787.793797566)),("Pittem", (518710.8788733787, 5650781.727620886)),\
    ("Plombires", (708776.5806071932, 5623730.094886116)),("Pont-Celles", (597935.2231810368, 5595403.095314185)),\
    ("Poperinge", (476935.300187478, 5635664.3848681655)),("Profondeville", (630756.4802517692, 5581942.712577484)),\
    ("Putte", (614194.1850707538, 5656647.881175696)),("Puurs", (591653.1356574316, 5658979.364287738)),\
    ("Péruwelz", (539690.5109855694, 5597710.9640553575)),("Quaregnon", (559767.3072031111, 5588081.2795319455)),\
    ("Quivrain", (549362.7960988614, 5582102.289368963)),("Quévy", (566978.3875872826, 5579449.22775478)),\
    ("Raeren", (294432.258541117, 5620507.395167005)),("Ramillies", (633422.4564655169, 5613071.581426517)),\
    ("Ranst", (610638.082172616, 5672334.356148241)),("Ravels", (639861.0325633386, 5697461.332900778)),\
    ("Rebecq", (580467.3305154644, 5614614.74266033)),("Remicourt", (665279.5509803816, 5617964.684365711)),\
    ("Rendeux", (679211.3987824183, 5566668.544253927)),("Retie", (644179.786342387, 5681512.444961982)),\
    ("Riemst", (682449.9287807208, 5631203.157501054)),("Rijkevorsel", (623029.3564705711, 5690228.937916604)),\
    ("Rixensart", (607446.2252226738, 5620038.175439725)),("Rochefort", (655431.1476666285, 5557908.504357325)),\
    ("Roeselare", (510833.7035413062, 5643353.061140569)),("Ronse", (542327.4515893657, 5622196.171145644)),\
    ("Roosdaal", (577702.536400828, 5631311.506172301)),("Rotselaar", (621350.9277126224, 5646308.718280662)),\
    ("Rouvroy", (680402.3662341178, 5489730.078435182)),("Ruiselede", (528037.6143334537, 5655461.214810729)),\
    ("Rumes", (521653.13149315456, 5599207.023050115)),("Rumst", (598824.8858393496, 5660657.998310145)),\
    ("Saint-Georges-sur-Meuse", (667484.995841394, 5608018.583145026)),("Saint-Ghislain", (556082.5298185392, 5592666.918296201)),\
    ("Saint-Hubert", (667307.1081179025, 5544647.600728106)),("Saint-Léger", (694200.0915016738, 5500099.13890926)),\
    ("Saint-Nicolas", (678757.8973475593, 5612097.190697245)),("Sainte-Ode", (681077.8559391772, 5546787.55139458)),\
    ("Sambreville", (614048.8496930053, 5589064.4004263105)),("Schelle", (593287.0139484141, 5665493.704677864)),\
    ("Scherpenheuvel-Zichem", (637987.1465551527, 5652032.733715686)),("Schilde", (608753.7349664095, 5678779.939491122)),\
    ("Schoten", (604685.1831343755, 5678695.236046782)),("Seneffe", (588802.7214346774, 5599790.0789689515)),\
    ("Seraing", (677817.457825929, 5607891.293152511)),("Silly", (566434.3055751983, 5610636.532253311)),\
    ("Sint-Amands", (586827.7626069026, 5656738.005163088)),("Sint-Genesius-Rode", (595235.3631521316, 5622893.457029036)),\
    ("Sint-Gillis-Waas", (578249.9516228213, 5676366.028919703)),("Sint-Katelijne-Waver", (608604.0916126317, 5658385.060419425)),\
    ("Sint-Laureins", (539761.1000902153, 5680371.893003103)),("Sint-Lievens-Houtem", (561568.3425118639, 5642339.411866918)),\
    ("Sint-Martens-Latem", (543265.6973288305, 5650928.858806003)),("Sint-Niklaas", (577782.5786390728, 5668951.094606879)),\
    ("Sint-Pieters-Leeuw", (586935.008054071, 5626830.544257595)),("Sint-Truiden", (653921.7937094783, 5630103.514344802)),\
    ("Sivry-Rance", (586906.4374365236, 5557129.049127102)),("Soignies", (575703.2596105831, 5602443.345655993)),\
    ("Sombreffe", (613451.0085317963, 5596370.909098546)),("Somme-Leuze", (665000.2351219534, 5574142.6108296625)),\
    ("Soumagne", (692267.2415513342, 5612842.891234575)),("Spa", (703293.2838118481, 5598151.151584416)),\
    ("Spiere-Helkijn", (525882.9620162761, 5619308.692229558)),("Sprimont", (689032.299669814, 5599845.777553624)),\
    ("Stabroek", (595822.8845282292, 5685941.7034558095)),("Staden", (501952.81066907436, 5644265.091620462)),\
    ("Stavelot", (707226.7597870728, 5588406.663526695)),("Steenokkerzeel", (605427.8627957962, 5642244.721037046)),\
    ("Stekene", (573939.8759999354, 5672598.23660537)),("Stoumont", (698086.2391031317, 5587053.780318166)),\
    ("Tellin", (660070.6984597209, 5550290.208459251)),("Temse", (583975.768419125, 5664410.177122174)),\
    ("Tenneville", (680731.8555800868, 5554043.368427765)),("Ternat", (582109.9140599217, 5635027.319623019)),\
    ("Tervuren", (608393.5585833356, 5631181.697628103)),("Tessenderlo", (645967.8979346468, 5659306.909391952)),\
    ("Theux", (700464.3350050913, 5599901.816134004)),("Thimister-Clermont", (702648.2664063598, 5614826.467991662)),\
    ("Thuin", (591674.5022639958, 5573935.994670938)),("Tielt", (525724.2409269473, 5651278.9230592325)),\
    ("Tielt-Winge", (632665.568530201, 5642714.208167629)),("Tienen", (635805.6159850748, 5631001.459228669)),\
    ("Tinlot", (668078.8395273163, 5594526.926812658)),("Tintigny", (680014.1788514217, 5506876.980390671)),\
    ("Tongeren", (673321.4837299814, 5628709.707623899)),("Torhout", (507006.8936846462, 5657246.97966746)),\
    ("Tournai", (527674.0011491819, 5606285.234780392)),("Tremelo", (632639.774570372, 5655230.736415349)),\
    ("Trois-Ponts", (703704.1479201929, 5581600.787459808)),("Trooz", (691757.4152648253, 5606067.021250146)),\
    ("Tubize", (584774.2315849639, 5615294.473926557)),("Turnhout", (635891.3975300194, 5686849.530170176)),\
    ("Vaux-sur-Sûre", (686590.028435206, 5534199.876302839)),("Verlaine", (662453.6552154457, 5608327.711559723)),\
    ("Verviers", (702435.5135248387, 5607136.092093882)),("Veurne", (477161.8748162058, 5655101.982750452)),\
    ("Vielsalm", (706758.9332605433, 5574694.1516467845)),("Villers-la-Ville", (608346.2867695517, 5603126.522828968)),\
    ("Villers-le-Bouillet", (658753.1975871779, 5607746.991090686)),("Vilvoorde", (601306.2971784525, 5643397.314502431)),\
    ("Viroinval", (617405.1733739679, 5547947.510578451)),("Virton", (686004.9354690092, 5493012.370716844)),\
    ("Vis", (689371.9195765884, 5622989.9234891655)),("Vleteren", (482034.6850820327, 5641204.400457046)),\
    ("Voeren", (698307.9134846914, 5625481.656421536)),("Vorselaar", (623430.7284796612, 5673549.299481291)),\
    ("Vosselaar", (631243.5863333449, 5686728.116719929)),("Vresse-sur-Semois", (637863.904759968, 5524640.431443772)),\
    ("Waarschoot", (541965.7003744561, 5666676.798558717)),("Waasmunster", (575850.260256819, 5661503.436032588)),\
    ("Wachtebeke", (560597.3168454176, 5668719.856275582)),("Waimes", (295793.1472395678, 5590883.013738769)),\
    ("Walcourt", (601923.7090006273, 5569496.210939877)),("Walhain", (620233.1596103493, 5609970.925971704)),\
    ("Wanze", (655466.7407699178, 5601773.093690348)),("Waregem", (525795.6499307471, 5636911.584212824)),\
    ("Waremme", (660085.0377169066, 5618381.714046196)),("Wasseiges", (643255.1830848937, 5609158.922301621)),\
    ("Waterloo", (597653.6363825062, 5619234.152995093)),("Wavre", (612555.466753636, 5619533.945850097)),\
    ("Welkenraedt", (708499.0042268409, 5615980.462436893)),("Wellen", (662543.3353356784, 5633826.6514770705)),\
    ("Wellin", (651196.545603743, 5549664.490603014)),("Wemmel", (591382.1188579932, 5641366.4583431855)),\
    ("Wervik", (503524.16577103874, 5626662.748726666)),("Westerlo", (632437.2240618558, 5663114.277244421)),\
    ("Wetteren", (561223.4035119576, 5648329.861189717)),("Wevelgem", (512129.3235223504, 5630067.289125665)),\
    ("Wezembeek-Oppem", (604415.4494541227, 5634192.786106912)),("Wichelen", (566267.5480813959, 5650249.336706901)),\
    ("Wielsbeke", (525395.6807045321, 5638143.9763324205)),("Wijnegem", (607047.8380816592, 5676886.184561762)),\
    ("Willebroek", (596368.813938084, 5656751.5742041785)),("Wingene", (516352.95684142393, 5655410.993649635)),\
    ("Wommelgem", (605965.3903840827, 5673159.183460471)),("Wortegem-Petegem", (537525.8116936097, 5635504.0338372355)),\
    ("Wuustwezel", (613059.4971031006, 5694637.872002422)),("Yvoir", (637346.942455538, 5576647.201409407)),\
    ("Zandhoven", (615737.7659280103, 5673737.279063287)),("Zaventem", (604359.6178547286, 5636972.626233945)),\
    ("Zedelgem", (509915.39032792975, 5664202.122433626)),("Zele", (572401.4191221825, 5657750.09435819)),\
    ("Zelzate", (557060.3738418543, 5672382.971567467)),("Zemst", (604132.2884060409, 5648281.131042825)),\
    ("Zingem", (542580.7189906462, 5639501.9902139595)),("Zoersel", (616318.5241988047, 5678946.020258919)),\
    ("Zomergem", (537705.8237035163, 5664786.588808259)),("Zonhoven", (664948.191486873, 5650596.678492324)),\
    ("Zonnebeke", (499528.3827136701, 5633511.521898722)),("Zottegem", (556294.1981034403, 5635473.260558299)),\
    ("Zoutleeuw", (647897.7458221783, 5632655.168916643)),("Zuienkerke", (508723.18381386925, 5678100.92842558)),\
    ("Zulte", (532397.6065278105, 5643131.598346917)),("Zutendaal", (680350.0516650463, 5645544.984660175)),\
    ("Zwalm", (550503.4509837793, 5636815.01206359)),("Zwevegem", (527022.9588602236, 5625430.548575103)),\
    ("Zwijndrecht", (593722.544393318, 5673844.430093279))]

def verify_order(communes):
    """Vérifie si une liste est ordonnée

    Args:
        communes (Iterable): la liste (de communes) à vérifier

    Returns:
        bool: True si la liste est ordonnée
    """
    for i in range(len(communes) - 1):  # -1 pourne pas alle en dehors de l'index
        if communes[i] > communes[i+1]:
            return False
    return True


def coordinate(commune, all_communes):
    """Renvoie les coordonées d'une commune

    Args:
        commune (str): le nom de la commune dont on veut les coordonés
        all_communes (list): La liste des communes avec le nom et les coordonés

    Returns:
        tuple: les coordonés (x,y)
    """
    first = 0
    last = len(all_communes) - 1
    found = False

    # Binary search :
    while first <= last and not found:
        middle = (first+last)//2
        if all_communes[middle][0] == commune:
            found = True
        else:
            if commune < all_communes[middle][0]:
                last = middle-1
            else:
                first = middle + 1

    if found:
        return all_communes[middle][1]
    else:
        return None


def distance_btw_coordinates(c1, c2):
    """Donne la distance entre 2 coordonés (x,y)

    Args:
        c1 (tuple): premier coordoné (x,y)
        c2 (tuple): deuxième coordonés (x,y)

    Returns:
        float: Distance entre les 2 coordonés
    """
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1] - c2[1])**2) # Grâce à la formume de distance entre 2 points

def distance(commune1, commune2, all_communes):
    """Donne la distance entre 2 communes

    Args:
        commune1 (str): Première commune
        commune2 (str): Deuxième commune
        all_communes (list): Liste de toutes les communes

    Returns:
        flaot: Distance entre les 2 communes (Renvoie 0 si les communes ne sont pas trouvées)
    """
    c1 = coordinate(commune1, all_communes)
    c2 = coordinate(commune2, all_communes)
    if c1 and c2:
        return distance_btw_coordinates(c1, c2)
    else:
        return 0


def tour_distance(communes, all_communes):
    """Renvoie la distance d'un tour des commmunes

    Args:
        communes (list): Les communes dont on veut faire le tour
        all_communes (list): Toutes les communes

    Returns:
        float: Distance du tour
    """
    total_distance = 0
    for c in range(len(communes)):
        if c + 1 == len(communes): # Si on est au dernier
            total_distance += distance(communes[c], communes[0], all_communes)
        else:
            total_distance += distance(communes[c],
                                       communes[c+1], all_communes)
    return total_distance

# Tests
def test_verifiy_order():
    unordered_list = ["Gembloux", "Bruxelles", "Liège"]
    ordered_list = ["Bruxelles", "Gembloux", "Liège"]
    assert verify_order(unordered_list) == False
    assert verify_order(ordered_list) == True


def test_coordinate():
    exemple = [("Gembloux", (5030, 1024)), ("Jardiland", (69, 420))]
    assert coordinate("Gembloux", exemple) == (5030, 1024)
    assert coordinate("Jardiland", exemple) == (69, 420)

def test_distance():
    assert distance_btw_coordinates((0,0), (0,200)) == 200

def test_tour_distance():
    exemple = [("G", (0,200)), ("T", (0,400))]
    assert tour_distance(["G", "T"], exemple) == 400

# On lance les tests
test_verifiy_order()
test_coordinate()
test_distance()
test_tour_distance()
