"""
Demo script to showcase the functionality of the summarize_figures function.
"""

from statistical_functions import summarize_figures

# Simple example with an arithmetic sequence
data = [2, 4, 6, 8, 10]
result = summarize_figures(data)

print("=" * 50)
print("STATISTICAL ANALYSIS DEMO")
print("=" * 50)
print(f"\nInput data: {data}")
print("\nSUMMARY:")
print(result['summary'])

print("\nDETAILED STATISTICS:")
stats = result['statistics']
for key, value in stats.items():
    if key != 'quartiles':
        print(f"{key}: {value}")
    else:
        print(f"quartiles: Q1={value['Q1']}, Q2={value['Q2']}, Q3={value['Q3']}")

print("\nORDER ANALYSIS:")
order = result['order_analysis']
for key, value in order.items():
    print(f"{key}: {value}")

print("\n" + "=" * 50)
print("End of demo")
print("=" * 50)