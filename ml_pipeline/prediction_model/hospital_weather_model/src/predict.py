from predict import predict_patient_count

sample_input = {
    "beds_available": 120,
    "staff_count": 45,
    "temperature": 32,
    "humidity": 60,
    "rainfall": 5
}

print(predict_patient_count(sample_input))
