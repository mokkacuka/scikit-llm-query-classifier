common_part1 = """Act like a professional in the {industry_or_category} industry.
You will be provided with the following information:
1. Search queries related to {industry_or_category}. The list of search queries is delimited with triple backticks.
2. List of {items} the search queries can be assigned to. The list is delimited with square brackets. The {items} in the list are enclosed in single quotes and comma separated.
"""

common_part2 = """Perform the following tasks:
1. Identify the {item} the provided search queries belong to with the highest probability.
2. Assign the provided search query to that {item} (e.g. "{example}": {example_value}).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.
List of classes: {{labels}}
Text sample: ```{{x}}```
Your JSON response:
"""
fine_tuning_sc_ingredients = """If the skincare ingredient or feature is explicitely mentioned in the query, do not infer a specific label and rather classify the {item} as {classification}.
"""

# Category dimension
ZERO_SHOT_CLF_PROMPT_TEMPLATE_CATEGORY = common_part1.format(industry_or_category="beauty", items="product categories") + common_part2.format(item="product category", classification="*Unknown Category*", example="mascara", example_value="Makeup")

# Skincare dimensions
ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM1 = common_part1.format(industry_or_category="skincare", items="skin concerns") + common_part2.format(item="skin concern", classification="*This query is not related to any skin concern known*", example="face cream", example_value="This query is not related to any skin concern known")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM2 = common_part1.format(industry_or_category="skincare", items="skincare ingredients or features") + fine_tuning_sc_ingredients.format(item="skincare ingredient or feature", classification="*This query is not related to any skincare ingredient or feature known*") + common_part2.format(item="skincare ingredient or feature", classification="*This query is not related to any skincare ingredient or feature known*", example="best vitamin c serum", example_value="Vitamin C")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM3 = common_part1.format(industry_or_category="skincare", items="skincare products") + common_part2.format(item="skincare product", classification="*This query is not related to any skincare product known*", example="best vitamin c serum", example_value="Serum")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM4 = common_part1.format(industry_or_category="skincare", items="skincare advices") + common_part2.format(item="skincare advice", classification="*This query is not related to any skincare advice*", example="best vitamin c serum", example_value="Best")

# Makeup dimensions
ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM1 = common_part1.format(industry_or_category="makeup", items="beauty concerns") + common_part2.format(item="beauty concern", classification="*This query is not related to any beauty concern known*", example="lip gloss", example_value="This query is not related to any beauty concern known")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM2 = common_part1.format(industry_or_category="makeup", items="ingredients or features") + common_part2.format(item="ingredient or feature", classification="*This query is not related to any makeup ingredient or feature known*", example="waterproof mascara", example_value="Waterproof")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM3 = common_part1.format(industry_or_category="makeup", items="makeup products") + common_part2.format(item="makeup product", classification="*This query is not related to any makeup product known*", example="red lipstick", example_value="Lipstick")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM4 = common_part1.format(industry_or_category="makeup", items="makeup advices or inspiration") + common_part2.format(item="makeup advice or inspiration", classification="*This query is not related to any makeup advice or inspiration known*", example="best red lipstick", example_value="Best")

# Hair dimensions
ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM1 = common_part1.format(industry_or_category="hair", items="hair concerns") + common_part2.format(item="hair concern", classification="*This query is not related to any hair concern known*", example="shampoo", example_value="This query is not related to any hair concern known")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM2 = common_part1.format(industry_or_category="hair", items="haircare ingredients or features") + common_part2.format(item="haircare ingredient or feature", classification="*This query is not related to any haircare ingredient or feature known*", example="dry hair shampo", example_value="Hydrating")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM3 = common_part1.format(industry_or_category="hair", items="haircare products") + common_part2.format(item="haircare product", classification="*This query is not related to any haircare product known*", example="dry shampoo", example_value="Dry Shampoo")
ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM4 = common_part1.format(industry_or_category="hair", items="hair advices or inspiration") + common_part2.format(item="hair advice or inspiration", classification="*This query is not related to any hair advice or inspiration known*", example="dry shampoo", example_value="Best")
