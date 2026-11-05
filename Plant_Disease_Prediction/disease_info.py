# Plant Disease Information & Treatment Database

CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

DISEASE_DETAILS = {
    'Apple___Apple_scab': {
        'crop': 'Apple',
        'condition': 'Apple Scab',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'symptoms': 'Olive-green to black velvety spots on leaves, yellowing leaves, corky brown lesions on fruit.',
        'organic_treatment': 'Apply sulfur or copper-based fungicides in early spring. Remove and compost fallen infected leaves.',
        'chemical_treatment': 'Use myclobutanil, captan, or mancozeb sprays at bud break and petal fall intervals.',
        'prevention': 'Prune trees for air circulation, avoid overhead watering, and plant scab-resistant cultivars like Honeycrisp or Liberty.'
    },
    'Apple___Black_rot': {
        'crop': 'Apple',
        'condition': 'Black Rot',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Circular purple-bordered leaf spots (frog-eye), black rotting fruit, and trunk cankers.',
        'organic_treatment': 'Prune out dead wood, mummified apples, and cankers during dormant season.',
        'chemical_treatment': 'Apply captan or thiophanate-methyl fungicides from tight cluster stage through harvest.',
        'prevention': 'Remove mummified fruit, sanitize pruning shears between cuts, and maintain tree vigor.'
    },
    'Apple___Cedar_apple_rust': {
        'crop': 'Apple',
        'condition': 'Cedar Apple Rust',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'Bright yellow-orange spots on upper leaf surfaces; tube-like structures releasing spores below.',
        'organic_treatment': 'Apply sulfur sprays at pink blossom stage. Remove nearby eastern red cedar galls within 1-2 miles.',
        'chemical_treatment': 'Apply myclobutanil or propiconazole when orange galls swell on nearby cedars.',
        'prevention': 'Plant rust-resistant apple varieties and manage surrounding juniper / cedar host plants.'
    },
    'Apple___healthy': {
        'crop': 'Apple',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Vibrant green foliage with smooth margins, free from spots, discoloration, or deformities.',
        'organic_treatment': 'Maintain balanced organic fertilization and regular mulching.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Continue routine scouting, adequate irrigation, and seasonal dormant oil sprays.'
    },
    'Blueberry___healthy': {
        'crop': 'Blueberry',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Glossy dark green leaves, uniform shape, no fungal spots or leaf chlorosis.',
        'organic_treatment': 'Maintain acidic soil pH (4.5 - 5.5) using pine bark mulch and elemental sulfur.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Ensure excellent soil drainage and avoid wetting foliage during irrigation.'
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'crop': 'Cherry',
        'condition': 'Powdery Mildew',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'White powdery fungal coating on leaves and young shoots, distorted and curling foliage.',
        'organic_treatment': 'Spray with potassium bicarbonate, dilute neem oil, or sulfur solutions.',
        'chemical_treatment': 'Apply quinoxyfen, myclobutanil, or triflumizole according to local spray guides.',
        'prevention': 'Prune canopy to promote sun penetration and rapid leaf drying after rain.'
    },
    'Cherry_(including_sour)___healthy': {
        'crop': 'Cherry',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Healthy dark green elliptical leaves with clean venation and sturdy petioles.',
        'organic_treatment': 'Maintain regular compost tea or organic nitrogen applications.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Practice dormant season sanitation and prevent insect wounding.'
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'crop': 'Corn (Maize)',
        'condition': 'Gray Leaf Spot',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Rectangular tan to gray lesions parallel to leaf veins, premature leaf death.',
        'organic_treatment': 'Incorporate crop residue deep into soil to speed microbial decomposition.',
        'chemical_treatment': 'Apply strobilurin (azoxystrobin) or triazole fungicides at tasseling stage (VT/R1).',
        'prevention': 'Rotate away from corn for at least 2 years and plant resistant hybrid seed.'
    },
    'Corn_(maize)___Common_rust_': {
        'crop': 'Corn (Maize)',
        'condition': 'Common Rust',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'Golden-brown to cinnamon-brown pustules scattered across both leaf surfaces.',
        'organic_treatment': 'Early planting to escape high late-season spore flights.',
        'chemical_treatment': 'Apply pyraclostrobin or tebuconazole if pustules appear before silking stage.',
        'prevention': 'Select corn hybrids with specific resistance genes (Rp genes).'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'crop': 'Corn (Maize)',
        'condition': 'Northern Leaf Blight',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Long, cigar-shaped grayish-green to tan lesions (1 to 6 inches long) on leaves.',
        'organic_treatment': 'Deep tillage to bury crop debris and reduce overwintering fungal inocula.',
        'chemical_treatment': 'Apply azoxystrobin + propiconazole fungicide at onset of symptoms.',
        'prevention': 'Use resistant hybrids (Ht genes) and practice strict crop rotation.'
    },
    'Corn_(maize)___healthy': {
        'crop': 'Corn (Maize)',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Broad deep-green leaves with clean, parallel venation and robust stalk attachment.',
        'organic_treatment': 'Maintain adequate nitrogen and organic matter levels.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Regular scouting during vegetative and reproductive growth phases.'
    },
    'Grape___Black_rot': {
        'crop': 'Grape',
        'condition': 'Black Rot',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Small reddish-brown circular leaf spots with dark margins; shriveled black mummified berries.',
        'organic_treatment': 'Apply copper fungicides during early bud development; destroy old fruit mummies.',
        'chemical_treatment': 'Apply mancozeb, myclobutanil, or tebuconazole before bloom and post-bloom.',
        'prevention': 'Keep vine canopy well aerated through shoot thinning and trellising.'
    },
    'Grape___Esca_(Black_Measles)': {
        'crop': 'Grape',
        'condition': 'Esca (Black Measles)',
        'status': 'Diseased',
        'severity': 'Severe',
        'symptoms': 'Tiger-stripe patterns on leaves (interveinal yellowing/browning), spotted fruit, wood necrosis.',
        'organic_treatment': 'Prune vines carefully; paint large cuts with protective pruning sealants.',
        'chemical_treatment': 'No curative chemical spray available; manage through wound protectors like thiophanate-methyl.',
        'prevention': 'Disinfect pruning shears, avoid pruning during wet weather, remove severely infected trunks.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'crop': 'Grape',
        'condition': 'Leaf Blight (Isariopsis)',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'Irregular brown spots with faint concentric rings, leading to premature defoliation.',
        'organic_treatment': 'Spray with Bordeaux mixture or copper oxychloride after fruit harvest.',
        'chemical_treatment': 'Apply azoxystrobin or carbendazim sprays when leaf spots first develop.',
        'prevention': 'Prune and burn infected leaves and maintain good vineyard sanitation.'
    },
    'Grape___healthy': {
        'crop': 'Grape',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Lush palmate green leaves without chlorosis, spots, or curled edges.',
        'organic_treatment': 'Apply compost mulch and ensure balanced potassium/magnesium nutrition.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Continue shoot positioning and proactive pest scouting.'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'crop': 'Orange (Citrus)',
        'condition': 'Citrus Greening (HLB)',
        'status': 'Diseased',
        'severity': 'Critical / Severe',
        'symptoms': 'Asymmetric blotchy yellow mottling across leaf veins, small lopsided bitter fruit with green ends.',
        'organic_treatment': 'Spray horticultural mineral oils or insecticidal soap to control psyllid vectors.',
        'chemical_treatment': 'Apply systemic insecticides (imidacloprid) targeting Asian citrus psyllids.',
        'prevention': 'Plant certified disease-free nursery stock and install physical protective insect netting.'
    },
    'Peach___Bacterial_spot': {
        'crop': 'Peach',
        'condition': 'Bacterial Spot',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'symptoms': 'Small angular purple-black spots that drop out leaving a "shot-hole" appearance; fruit cracking.',
        'organic_treatment': 'Apply fixed copper sprays during dormancy and early leaf bud stages.',
        'chemical_treatment': 'Use oxytetracycline (Mycoshield) or copper hydroxide formulations at petal fall.',
        'prevention': 'Plant resistant peach cultivars and avoid excessive nitrogen fertilizer.'
    },
    'Peach___healthy': {
        'crop': 'Peach',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Lanceolate smooth green leaves with finely serrated margins and clean surfaces.',
        'organic_treatment': 'Maintain good irrigation and organic fertilization in root zones.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Inspect trees for borers and apply dormant protective copper spray.'
    },
    'Pepper,_bell___Bacterial_spot': {
        'crop': 'Bell Pepper',
        'condition': 'Bacterial Spot',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Water-soaked spots turning dark brown with yellow halos, blistered lesions on peppers.',
        'organic_treatment': 'Spray copper octanoate + Bacillus subtilis biofungicide.',
        'chemical_treatment': 'Apply copper hydroxide mixed with mancozeb for increased bacterial suppression.',
        'prevention': 'Use certified pathogen-free seeds, drip irrigation, and avoid handling plants when wet.'
    },
    'Pepper,_bell___healthy': {
        'crop': 'Bell Pepper',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Dark glossy green, oval-to-lanceolate leaves with uniform texture and no spots.',
        'organic_treatment': 'Provide steady soil moisture and organic compost tea feeds.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Practice 3-year solanaceous crop rotation.'
    },
    'Potato___Early_blight': {
        'crop': 'Potato',
        'condition': 'Early Blight',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'symptoms': 'Dark brown to black spots with concentric rings ("target board" pattern) on older leaves.',
        'organic_treatment': 'Spray with copper sulfate or potassium bicarbonate solutions. Prune lower infected leaves.',
        'chemical_treatment': 'Apply chlorothalonil, azoxystrobin, or difenoconazole every 7-14 days.',
        'prevention': 'Ensure proper plant spacing, drip irrigation, and remove solanaceous weed hosts.'
    },
    'Potato___Late_blight': {
        'crop': 'Potato',
        'condition': 'Late Blight (Phytophthora)',
        'status': 'Diseased',
        'severity': 'Critical / Severe',
        'symptoms': 'Large dark water-soaked lesions that rapidly turn black; white fuzzy mold on underside in humid air.',
        'organic_treatment': 'Immediately destroy and bury heavily infected plants. Apply copper fungicide preventively.',
        'chemical_treatment': 'Apply systemic oomycete fungicides: metalaxyl, cymoxanil, or mandipropamid.',
        'prevention': 'Plant certified disease-free seed tubers and eliminate volunteer potato cull piles.'
    },
    'Potato___healthy': {
        'crop': 'Potato',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Compound green leaves with clean leaflets, no lesions, yellowing, or edge curl.',
        'organic_treatment': 'Hill potatoes with straw mulch and maintain consistent moisture.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Scout twice weekly during warm, humid weather.'
    },
    'Raspberry___healthy': {
        'crop': 'Raspberry',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Compound pinnate green leaves with serrated margins, clean silvery undersides.',
        'organic_treatment': 'Mulch canes with woodchips and provide balanced potassium.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Prune spent second-year floricanes post-harvest to enhance airflow.'
    },
    'Soybean___healthy': {
        'crop': 'Soybean',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Trifoliate clean green leaves with strong petiole attachment and zero rust or mosaic spots.',
        'organic_treatment': 'Inoculate seed with Bradyrhizobium japonicum for organic nitrogen fixation.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Maintain weed control and avoid soil compaction.'
    },
    'Squash___Powdery_mildew': {
        'crop': 'Squash',
        'condition': 'Powdery Mildew',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'Talcum-powder-like white fungal growth covering upper and lower leaf surfaces; yellowing leaves.',
        'organic_treatment': 'Spray with 40% milk and 60% water solution, potassium bicarbonate, or horticultural oil.',
        'chemical_treatment': 'Apply myclobutanil, triflumizole, or chlorothalonil upon first appearance.',
        'prevention': 'Plant mildew-resistant squash varieties and ensure full sunlight exposure.'
    },
    'Strawberry___Leaf_scorch': {
        'crop': 'Strawberry',
        'condition': 'Leaf Scorch',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'Irregular purplish-brown blotches without yellow halos, leaves curl upward and appear scorched.',
        'organic_treatment': 'Mow and rake out old strawberry foliage post-harvest; apply copper fungicide in autumn.',
        'chemical_treatment': 'Apply captan or thiophanate-methyl during early bloom and post-harvest.',
        'prevention': 'Use drip irrigation, avoid overcrowding runner plants, and mulch beds with clean straw.'
    },
    'Strawberry___healthy': {
        'crop': 'Strawberry',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Three-leaflet fan-shaped bright green leaves with serrated edges and healthy gloss.',
        'organic_treatment': 'Apply pine needle or straw mulch and fish emulsion fertilizer.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Renew strawberry beds every 3-4 years.'
    },
    'Tomato___Bacterial_spot': {
        'crop': 'Tomato',
        'condition': 'Bacterial Spot',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Small dark greasy or water-soaked spots with yellow halos on leaves; raised scabby spots on fruit.',
        'organic_treatment': 'Spray fixed copper formulations combined with biological Serenade (Bacillus subtilis).',
        'chemical_treatment': 'Apply copper octanoate + mancozeb tank mix for improved efficacy.',
        'prevention': 'Avoid overhead sprinklers, sanitize stakes/cages, and practice 3-year crop rotation.'
    },
    'Tomato___Early_blight': {
        'crop': 'Tomato',
        'condition': 'Early Blight',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Brown-black target-ring spots on lowest leaves first, progressing upward; yellowing leaf canopy.',
        'organic_treatment': 'Prune lower leaves up to 18 inches off the ground. Spray copper or biofungicide.',
        'chemical_treatment': 'Apply chlorothalonil, mancozeb, or azoxystrobin on 7-10 day spray schedules.',
        'prevention': 'Mulch soil surface with straw or plastic to prevent soil splash onto lower foliage.'
    },
    'Tomato___Late_blight': {
        'crop': 'Tomato',
        'condition': 'Late Blight',
        'status': 'Diseased',
        'severity': 'Critical / Severe',
        'symptoms': 'Large greasy brown-black patches on leaves and stems; white fungal spores under humid conditions.',
        'organic_treatment': 'Immediately pull and dispose of infected plants in sealed bags (do not compost).',
        'chemical_treatment': 'Apply mandipropamid, chlorothalonil, or metalaxyl preventively during cool, wet weather.',
        'prevention': 'Plant resistant varieties (e.g., Mountain Magic, Defiant PHR) and monitor regional blight alerts.'
    },
    'Tomato___Leaf_Mold': {
        'crop': 'Tomato',
        'condition': 'Leaf Mold',
        'status': 'Diseased',
        'severity': 'Moderate',
        'symptoms': 'Pale green or yellow spots on upper leaf surfaces with olive-green to brown velvety mold below.',
        'organic_treatment': 'Increase greenhouse ventilation to reduce relative humidity below 85%.',
        'chemical_treatment': 'Apply copper sulfate or chlorothalonil sprays targeting leaf undersides.',
        'prevention': 'Provide adequate plant spacing, prune suckers, and use horizontal airflow fans.'
    },
    'Tomato___Septoria_leaf_spot': {
        'crop': 'Tomato',
        'condition': 'Septoria Leaf Spot',
        'status': 'Diseased',
        'severity': 'High',
        'symptoms': 'Numerous small circular spots with dark brown margins and gray centers dotted with tiny black fruiting bodies.',
        'organic_treatment': 'Remove affected bottom leaves immediately. Spray with liquid copper fungicide.',
        'chemical_treatment': 'Apply chlorothalonil or mancozeb at the first sign of lower leaf spotting.',
        'prevention': 'Stake plants upright, mulch heavily, and do not work in wet tomato patches.'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'crop': 'Tomato',
        'condition': 'Two-Spotted Spider Mite',
        'status': 'Diseased / Pest',
        'severity': 'High',
        'symptoms': 'Fine yellow stippling or bronzing of leaves; delicate silk webbing visible on leaf undersides.',
        'organic_treatment': 'Release predatory mites (Phytoseiulus persimilis), spray with insecticidal soap or neem oil.',
        'chemical_treatment': 'Apply miticides like bifenazate or abamectin targeting leaf undersides.',
        'prevention': 'Avoid dusty conditions, keep plants well-watered, and avoid broad-spectrum pyrethroid insecticides.'
    },
    'Tomato___Target_Spot': {
        'crop': 'Tomato',
        'condition': 'Target Spot (Corynespora)',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'symptoms': 'Brown circular lesions with concentric rings and yellow halos on leaves, stems, and fruit.',
        'organic_treatment': 'Improve plant airflow, prune dense foliage, and apply copper-based fungicides.',
        'chemical_treatment': 'Apply azoxystrobin + difenoconazole or boscalid formulations.',
        'prevention': 'Rotate away from solanaceous and cucurbit crops; keep foliage dry.'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'crop': 'Tomato',
        'condition': 'Yellow Leaf Curl Virus (TYLCV)',
        'status': 'Diseased / Viral',
        'severity': 'Severe',
        'symptoms': 'Severe upward curling and cupping of leaflets, marked yellowing of margins, stunted bushy plant growth.',
        'organic_treatment': 'Cover seedlings with fine insect-exclusion fleece to block whitefly vectors.',
        'chemical_treatment': 'Control whitefly populations using systemic dinotefuran or insecticidal soaps (no virus cure).',
        'prevention': 'Plant TYLCV-resistant cultivars and install yellow sticky traps to monitor whiteflies.'
    },
    'Tomato___Tomato_mosaic_virus': {
        'crop': 'Tomato',
        'condition': 'Mosaic Virus (ToMV)',
        'status': 'Diseased / Viral',
        'severity': 'Severe',
        'symptoms': 'Mottled dark and light green mosaic patterns on leaves, leaf distortion (shoestring effect), stunted growth.',
        'organic_treatment': 'No cure exists. Immediately rouge out and destroy all infected plants.',
        'chemical_treatment': 'No chemical cure. Wash hands with milk or soap before handling seedlings.',
        'prevention': 'Purchase certified virus-free seed, sanitize all tools with 10% bleach, and avoid tobacco use near plants.'
    },
    'Tomato___healthy': {
        'crop': 'Tomato',
        'condition': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'symptoms': 'Deep green serrated leaflets with crisp texture, zero lesions, and robust petioles.',
        'organic_treatment': 'Maintain steady watering and apply organic calcium/potassium supplements.',
        'chemical_treatment': 'No treatment required.',
        'prevention': 'Regular scouting, proper trellising, and organic mulch cover.'
    }
}

