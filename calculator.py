# AQUA-SERVER: Термодинамический калькулятор опреснения
# Разработано для хакатона VentureHack 2026 (Трек: Open Innovation)

def calculate_thermal_energy(mass_flow, temp_out, temp_in):
    """
    Рассчитывает количество полученной тепловой энергии (Q = m * c * dT)
    c - удельная теплоемкость воды/теплоносителя (~4.187 кДж/(кг*°C))
    """
    c = 4.187 
    dT = temp_out - temp_in
    if dT <= 0:
        return 0, "Ошибка: Температура на выходе должна быть выше, чем на входе."
    
    # Q в киловаттах (кВт), если масса в кг/с
    Q = mass_flow * c * dT
    return Q, None

print("=== Симуляция теплообмена AQUA-SERVER ===")
# Примерные входные данные для теста
mass_flow_rate = 5.0  # Скорость протока жидкости (кг/сек)
t_inlet = 45.0        # Температура на входе в сервер (°C)
t_outlet = 75.0       # Температура после охлаждения процессоров AI (°C)

energy, error = calculate_thermal_energy(mass_flow_rate, t_outlet, t_inlet)

if error:
    print(error)
else:
    print(f"Поток жидкости: {mass_flow_rate} кг/с")
    print(f"Нагрев теплоносителя процессорами: с {t_inlet}°C до {t_outlet}°C (dT = {t_outlet - t_inlet}°C)")
    print(f"Утилизируемая тепловая энергия (Q): {energy:.2f} кВт")
    print("--------------------------------------------------")
    print("Энергия успешно перенаправлена на контур мембранной дистилляции.")
