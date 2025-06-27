"""
Edge cases: 

case 1: empty input
[], => []

case 2: Has trendy material
[
    {
        'name': 'startup A', 
        'materials': ['Carbon', 'Nitrogen']
    },

    {
        'name': 'startup B', 
        'materials': ['Water', 'Nitrogen', 'Copper', 'Gold']
    },
] => ['Nitrogen']

case 3: No trendy Material
[
    {
        'name': 'startup A', 
        'materials': ['Carbon', 'Nitrogen']
    },

    {
        'name': 'startup B', 
        'materials': ['Water', 'Copper', 'Gold']
    },
] => []


Time & Space complexity

Step1: Counting materials frequency across all brands
n: number of brands
m: average number of materials per brand
s: average length of each string in materials per brand
time: O(n * m * s)
space: O(n * m * s)

Step2: Collecting trendy materials by looping through the resulted dictionary


"""

def find_trending_materials(brands):
    # collect material frequencies
    frequencies = {}
    res = []
    for brand in brands:
        for material in brand["materials"]:
            frequencies[material] = frequencies.get(material, 0) + 1
            
    # get trendy materials == matrials with frequency greater than 1
    for material in frequencies:
        if frequencies[material] > 1:
            res.append(material)

    return res

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))