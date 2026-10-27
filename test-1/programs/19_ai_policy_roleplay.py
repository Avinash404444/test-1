print("AI POLICY ROLEPLAY SIMULATION")
print("Role: You are an AI Policy Maker")
print("\nScenario:")
print("A college plans to use AI for student attendance.")
print("Choose an AI policy:")
print("1. Use facial recognition without consent")
print("2. Use AI with student consent")
print("3. Do not use AI for attendance")
choice = input("\nEnter your choice (1-3): ")
if choice == "1":
    print("\nDecision: Privacy risk")
    print("Feedback: Using facial recognition without")
    print("consent raises privacy and ethical concerns.")
elif choice == "2":
    print("\nDecision: Consent-based AI")
    print("Feedback: Consent and transparency help")
    print("protect student privacy.")
elif choice == "3":
    print("\nDecision: Avoid AI attendance")
    print("Feedback: This avoids some privacy risks.")
else:
    print("Invalid choice. Please select 1, 2 or 3.")
