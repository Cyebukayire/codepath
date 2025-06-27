
"""
Steps:
loop through brand
count material frequency in a set

n: number of brands
m: average number of materials per brand
s: average length of each string in materials

Time complexity: O(n * m * s) // The hash key loop up is actually O(s)
Space complexity: O(n * m * s)
"""
def count_material_usage(brands):
    material_frequency = {}
    for brand in brands:
        for material in brand["materials"]:
            material_frequency[material] = material_frequency.get(material, 0) + 1

    return material_frequency
    

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

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))