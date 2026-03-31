import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def create_dataset():
    data = {
        "difficulty": [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 5, 4, 2, 3, 1, 4, 5, 3, 2, 4],
        "days_left": [15, 12, 10, 7, 3, 2, 5, 8, 14, 20, 1, 4, 11, 6, 18, 9, 2, 7, 13, 5],
        "preparation": [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 1, 2, 4, 3, 5, 2, 1, 3, 4, 2],
        "importance": [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 5, 4, 2, 3, 1, 4, 5, 3, 2, 4],
        "study_hours": [1, 2, 4, 7, 12, 11, 8, 5, 2, 1, 13, 9, 3, 6, 1, 8, 12, 5, 2, 7]
    }
    return pd.DataFrame(data)


def train_model(df):
    X = df[["difficulty", "days_left", "preparation", "importance"]]
    y = df["study_hours"]

    model = DecisionTreeRegressor(random_state=42)
    model.fit(X, y)
    return model


def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def rule_based_adjustment(predicted_hours, days_left, preparation):
    adjusted_hours = predicted_hours

    if days_left <= 3:
        adjusted_hours += 1

    if preparation >= 4:
        adjusted_hours -= 0.5

    return max(round(adjusted_hours, 2), 1)


def get_priority_level(hours):
    if hours <= 2:
        return "Low"
    elif hours <= 5:
        return "Moderate"
    elif hours <= 8:
        return "High"
    return "Very High"


def get_advice(priority):
    if priority == "Very High":
        return "Start immediately and revise daily."
    elif priority == "High":
        return "Give this subject strong focus."
    elif priority == "Moderate":
        return "Maintain regular study sessions."
    return "Light revision should be enough."


def predict_study_time(model, difficulty, days_left, preparation, importance):
    input_data = pd.DataFrame({
        "difficulty": [difficulty],
        "days_left": [days_left],
        "preparation": [preparation],
        "importance": [importance]
    })

    predicted_hours = model.predict(input_data)[0]
    final_hours = rule_based_adjustment(predicted_hours, days_left, preparation)
    return final_hours


def display_results(results):
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by="Recommended Study Time (hours)", ascending=False)

    print("\n" + "=" * 95)
    print("FINAL STUDY PLAN")
    print("=" * 95)
    print(results_df.to_string(index=False))
    print("=" * 95)

    total_hours = results_df["Recommended Study Time (hours)"].sum()
    print(f"\nTotal Recommended Study Time for All Subjects: {round(total_hours, 2)} hours")


def main():
    print("=" * 60)
    print("                SMART STUDY TIME RECOMMENDER")
    print("=" * 60)

    df = create_dataset()
    model = train_model(df)

    num_subjects = get_valid_input("Enter the number of subjects: ", 1, 20)

    results = []

    for i in range(1, num_subjects + 1):
        print(f"\nEntering details for Subject {i}")
        print("-" * 40)

        subject_name = input("Enter subject name: ").strip()
        difficulty = get_valid_input("Enter subject difficulty (1-5): ", 1, 5)
        days_left = get_valid_input("Enter days left before exam (1-30): ", 1, 30)
        preparation = get_valid_input("Enter preparation level (1-5): ", 1, 5)
        importance = get_valid_input("Enter subject importance (1-5): ", 1, 5)

        hours = predict_study_time(model, difficulty, days_left, preparation, importance)
        priority = get_priority_level(hours)
        advice = get_advice(priority)

        results.append({
            "Subject": subject_name,
            "Difficulty": difficulty,
            "Days Left": days_left,
            "Preparation": preparation,
            "Importance": importance,
            "Recommended Study Time (hours)": hours,
            "Priority": priority,
            "Advice": advice
        })

    display_results(results)


if __name__ == "__main__":
    main()
