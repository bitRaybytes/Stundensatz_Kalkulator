from tkinter import *
import tkinter
from root_styles import *

# Initializing Frame with title, height and width
root = Tk()
root.title("Stundensatzkalkulator")
root.geometry("700x700")
frame = Frame(root, bg="green").grid(row=1, column=0)
scrollbar = Scrollbar(root).grid(row=0, column=2, rowspan=40)
root.config(bg="lightblue")

# heading and subheading
header_label = Label(frame, text="Kalkuliere deinen Stundenstatz als Selbständiger", font=font_18)
header_label.grid(row=0, column=0, columnspan=2, padx=padx, pady=pady)
subheading_label = Label(frame, text="Bitte trage deine eigenen Zahlen ein", font=font_14)
subheading_label.grid(row=1, column=0,columnspan=2, padx=padx, pady=pady)

# costs section
costs_label = Label(frame, text="Kosten:", foreground="red", font=font_14)
costs_label.grid(row=2, column=0, padx=padx, pady=pady)

grossvalue_label = Label(frame, text="gewünschtes Bruttogehalt:", font=font_14, justify="right")
grossvalue_label.grid(row=4, column=0, padx=padx, pady=pady)
grossvalue_entry = Entry(frame, bg="gray")
grossvalue_entry.grid(row=4, column=1, padx=padx, pady=pady)

socialinsurance_label = Label(frame, text="Sozialversicherungssatz in %:", font=font_14)
socialinsurance_label.grid(row=5, column=0, padx=padx, pady=pady)
socialinsurance_entry = Entry(frame, bg="gray")
socialinsurance_entry.grid(row=5, column=1, padx=padx, pady=pady)
socialinsurance_entry.insert(0,"20")
    # place an image, after click a tooltip will appear
socialinsurance_label_entry_info = Label(frame, text="AS TOOLTIP: Hier kannst du deinen eigenen Prozentsatz \neingeben, ansonsten rechnen wir mit pauschal 20%")
socialinsurance_label_entry_info.grid(row=5, column=2, padx=padx, pady=pady)

occupational_rate_label = Label(frame, text="Berufsunfähigkeitsversicherung:", font=font_14)
occupational_rate_label.grid(row=6, column=0, padx=padx, pady=pady) 
occupatinal_rate_entry = Entry(frame, bg="gray")
occupatinal_rate_entry.grid(row=6, column=1, padx=padx, pady=pady)
occupatinal_rate_entry.insert(0,"75.0") 

retirement_planning_label = Label(frame, text="Altersvorsorge (10%): ")
retirement_planning_label.grid(row=7, column=0, padx=padx, pady=pady)

subtotal_label = Label(frame, text="Zwischensumme: ", font=font_14)
subtotal_label.grid(row=8, column=0, padx=padx, pady=pady)


# utilization section
utilization_header_label = Label(frame, text="Auslastung im Jahr:", foreground="red", font=font_14)
utilization_header_label.grid(row=9, column=0, padx=padx, pady=pady)
calendar_days_label = Label(frame, text="Kalendertage: (Standard: 360)", font=font_14)
calendar_days_label.grid(row=10, column=0, padx=padx, pady=pady)
calendar_days_entry = Entry(frame, show="360", bg="gray")
calendar_days_entry.grid(row=10, column=1, padx=padx, pady=pady)
weekends_label = Label(frame, text="Wochenenden: (Standard: 104)", font=font_14)
weekends_label.grid(row=11, column=0, padx=padx, pady=pady)
weekends_entry = Entry(frame, show= "104", bg="gray")
weekends_entry.grid(row=11, column=1, padx=padx, pady=pady)

holidays_label = Label(frame, text="Feiertage:", font=font_14)
holidays_label.grid(row=12, column=0, padx=padx, pady=pady)
vacation_label = Label(frame, text="Urlaubstage:", font=font_14)
vacation_label.grid(row=13, column=0, padx=padx, pady=pady)
sickleave_label = Label(frame, text="geschätzter Krankenstand:", font=font_14)
sickleave_label.grid(row=14, column=0, padx=padx, pady=pady)
education_label = Label(frame, text="Weiterblidungsmaßnahmen:", font=font_14)
education_label.grid(row=15, column=0, padx=padx, pady=pady)

holidays_entry = Entry(frame, bg="gray")
holidays_entry.grid(row=12, column=1, padx=padx, pady=pady)
vacation_entry = Entry(frame, bg="gray")
vacation_entry.grid(row=13, column=1, padx=padx, pady=pady)
sickleave_entry = Entry(frame, bg="gray")
sickleave_entry.grid(row=14, column=1, padx=padx, pady=pady)
education_entry = Entry(frame, bg="gray")
education_entry.grid(row=15, column=1, padx=padx, pady=pady)

work_days_year_label = Label(frame, text="Arbeitstage pro Jahr: ", font=font_14)
work_days_year_label.grid(row=16, column=0, padx=padx, pady=pady)
work_days_year_result_label = Label(frame, text="input rein", font=font_14)
work_days_year_result_label.grid(row=16, column=1, padx=padx, pady=pady)

utilization_label = Label(frame, text="geschätze Auslastung in %:", font=font_14)
utilization_label.grid(row=17, column=0, padx=padx, pady=pady)
utilization_entry = Entry(frame, bg="gray")
utilization_entry.grid(row=17, column=1, padx=padx, pady=pady)


productivity_label = Label(frame, text="Produktivität im Monat: ", font=font_14)
productivity_label.grid(row=18, column=0, padx=padx, pady=pady)
productivity_result_label = Label(frame, text="input rein", font=font_14)
productivity_result_label.grid(row=18, column=1, padx=padx, pady=pady)

# further costs section
further_costs_label = Label(frame, text="Weitere Kosten", foreground="red", font=font_14)
further_costs_label.grid(row=19, column=0, padx=padx, pady=pady)
further_costs_info_label = Label(frame, text="Trage eine Kosten für dieses Jahr ein:", font=font_14)
further_costs_info_label.grid(row=20, column=0, padx=padx, pady=pady)

rent_label = Label(frame, text="Miete:", font=font_14)
rent_label.grid(row=21, column=0, padx=padx, pady=pady)
rent_entry = Entry(frame, bg="gray")
rent_entry.grid(row=21, column=1, padx=padx, pady=pady)
marketing_label = Label(frame, text="Marketing:", font=font_14)
marketing_label.grid(row=22,column=0, padx=padx, pady=pady)
marketing_entry = Entry(frame, bg="gray")
marketing_entry.grid(row=22, column=1, padx=padx, pady=pady)
management_label = Label(frame, text="Verwaltung:", font=font_14)
management_label.grid(row=23, column=0, padx=padx, pady=pady)
management_entry = Entry(frame, bg="gray")
management_entry.grid(row=23, column=1, padx=padx, pady=pady)
supplier_label = Label(frame, text="Lieferanten:", font=font_14)
supplier_label.grid(row=24, column=0, padx=padx, pady=pady)
supplier_entry = Entry(frame, bg="gray")
supplier_entry.grid(row=24, column=1, padx=padx, pady=pady)
comInsurance_label = Label(frame, text="Betriebliche Versicherung:", font=font_14)
comInsurance_label.grid(row=25, column=0, padx=padx, pady=pady)
comInsurance_entry = Entry(frame, bg="gray")
comInsurance_entry.grid(row=25, column=1, padx=padx, pady=pady)
finance_label = Label(frame, text="Finanzierungen:", font=font_14)
finance_label.grid(row=26, column=0, padx=padx, pady=pady)
finance_entry = Entry(frame, bg="gray")
finance_entry.grid(row=26, column=1, padx=padx, pady=pady)
workUtilities_label = Label(frame, text="Werkzeuge/Software:", font=font_14)
workUtilities_label.grid(row=27, column=0, padx=padx, pady=pady)
workUtilities_entry = Entry(frame, bg="gray")
workUtilities_entry.grid(row=27, column=1, padx=padx, pady=pady)
extras_label = Label(frame, text="sonstige Ausgaben:", font=font_14)
extras_label.grid(row=28, column=0, padx=padx, pady=pady)
extras_entry = Entry(frame, bg="gray")
extras_entry.grid(row=28, column=1, padx=padx, pady=pady)
taxes_label = Label(frame, text="betriebliche Steuern:", font=font_14)
taxes_label.grid(row=29, column=0, padx=padx, pady=pady)
taxes_entry = Entry(frame, bg="gray")
taxes_entry.grid(row=29, column=1, padx=padx, pady=pady)
total_costs_label = Label(frame, text="Gesamtkosten:", font=font_14)
total_costs_label.grid(row=30, column=0, padx=padx, pady=pady)
total_costs_result_label = Label(frame, text="input rein")
total_costs_result_label.grid(row=30, column=1, padx=padx, pady=pady)

# results section
hourly_rate_header_label = Label(frame, text="Stundensatz errechnen:", font=font_14)
hourly_rate_header_label.grid(row=31, column=0, padx=padx, pady=pady)
hourly_rate_header_entry = Entry(frame, bg="gray")
hourly_rate_header_entry.grid(row=31, column=1, padx=padx, pady=pady)
hourly_rate_header_result_label = Label(frame, text="Input rein", font=font_14)
hourly_rate_header_result_label.grid(row=32, column=0, padx=padx, pady=pady)
hourly_rate_header_result_entry = Entry(frame, bg="gray")
hourly_rate_header_result_entry.grid(row=32, column=1, padx=padx, pady=pady)
billable_work_label = Label(frame, text="Abrechenbare Arbeitsstunden:", font=font_14)
billable_work_label.grid(row=33, column=0, padx=padx, pady=pady)
billable_work_entry = Entry(frame, bg="gray")
billable_work_entry.grid(row=33, column=1, padx=padx, pady=pady)
each_day_label = Label(frame, text="Pro Arbeitstag:", font=font_14)
each_day_label.grid(row=34, column=0, padx=padx, pady=pady)
each_day_entry = Entry(frame, bg="gray")
each_day_entry.grid(row=34, column=1, padx=padx, pady=pady)
working_hours_daily_label = Label(frame, text="Arbeitsstunden pro Tag:", font=font_14)
working_hours_daily_label.grid(row=34, column=0, padx=padx, pady=pady)   
working_hours_daily_entry = Entry(frame, bg="gray")
working_hours_daily_entry.grid(row=34, column=1, padx=padx, pady=pady)

billing_label = Label(frame, text="Finanzierungskosten in %:", font=font_14)
billing_label.grid(row=35, column=0, padx=padx, pady=pady)
billing_entry = Entry(frame, bg="gray")
billing_entry.grid(row=35, column=1, padx=padx, pady=pady)
revenue_label = Label(frame, text="Gewinnmarge in %:", font=font_14)
revenue_label.grid(row=36, column=0, padx=padx, pady=pady)
revenue_entry = Entry(frame, bg="gray")
revenue_entry.grid(row=36, column=1, padx=padx, pady=pady)
vat_label = Label(frame, text="zzgl. 19% MwSt.:", font=font_14)
vat_label.grid(row=37, column=0, padx=padx, pady=pady)
vat_entry = Entry(frame, bg="gray")
vat_entry.grid(row=37, column=1, padx=padx, pady=pady)

def calculate_grossvalue():
    global error_window
    global subtotal
    try:
        grossvalue = float(grossvalue_entry.get())
        socialinsurance_entry_value = float(socialinsurance_entry.get())
        socialinsurance_rate = 20 # change to another integer, only change, if si-rate is different or known
        socialinsurance = (grossvalue * socialinsurance_entry_value) / 100
        occupational_rate = float(75) # prefix for value is Euro
        occupational_result = (grossvalue *10) /100

        subtotal = (grossvalue + socialinsurance_rate + occupational_rate + occupational_result)
        # string = subtotal + "daraus Sozialabgaben: " + socialinsurance + ", "
        return subtotal, socialinsurance
    except:
        def error_window():
            error_window = Toplevel(root)
            error_window.geometry("100x100")
            error_message = "Bitte Werte eintragen!"
            error_message = Label(error_window, text=error_message)
            error_message.pack()
            return error_window
            
            
            

calculate_btn = Button(frame, text="Berechnen", command= lambda: [ calculate_grossvalue(), change_values()]).grid(row=0, column=2)
delete_btn = Button(frame, text="Löschen").grid(row=0, column=3)

def change_values():
   
    retirement_planning_result_label = Label(frame, text=f"")
    retirement_planning_result_label.grid(row=7, column=1, padx=padx, pady=pady)
    subtotal_result_label = Label(frame, text=f"{calculate_grossvalue()}", font=font_14)
    subtotal_result_label.grid(row=8, column=1, padx=padx, pady=pady)

root.mainloop()