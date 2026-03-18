# LIME Quick Reference

## TabularExplainer
- **Purpose:** Explains black-box classifiers for tabular data.
- **Key Methods:**
  - `fit`: Fit the explainer on your dataset.
  - `explain_instance`: Generates explanations for specific instances.

## ImageExplainer
- **Purpose:** Explains image classifiers by generating pixel-wise importance scores.
- **Key Methods:**
  - `explain_instance`: Explains predictions for specific images.

## TextExplainer
- **Purpose:** Provides explanations for text classifiers, showing the contribution of each word.
- **Key Methods:**
  - `explain_instance`: Generates explanations for specific text instances.

## Interpretation Techniques
1. **Local Explanations:** Focus on explaining individual predictions.
2. **Global Explanations:** Provide insights into model behavior across the entire dataset.
3. **Feature Importance:** Rank features based on their contribution to the model's predictions.

---