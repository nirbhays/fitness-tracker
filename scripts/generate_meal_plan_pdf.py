"""
Nutrition & Meal Plan PDF Generator
Generates a comprehensive PDF for the evidence-based meal plan
"""

from fpdf import FPDF
from datetime import datetime
import os


class MealPlanPDF(FPDF):
    """Generate a PDF for the nutrition and meal plan"""
    
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(34, 139, 34)  # Forest green
        self.cell(0, 10, 'EVIDENCE-BASED NUTRITION & MEAL PLAN', 0, 1, 'C')
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, 'Optimized for Fat Loss + Muscle Gain (Body Recomposition)', 0, 1, 'C')
        self.ln(3)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Generated: {datetime.now().strftime("%Y-%m-%d")}', 0, 0, 'C')
        
    def add_section_title(self, title, color=(34, 139, 34)):
        self.ln(5)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*color)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_text_color(0, 0, 0)
        
    def add_subsection_title(self, title, color=(70, 130, 180)):
        self.ln(3)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(*color)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_text_color(0, 0, 0)
        
    def add_info_box(self, text, fill_color=(240, 255, 240)):
        self.set_fill_color(*fill_color)
        self.set_draw_color(34, 139, 34)
        self.set_font('Helvetica', 'B', 10)
        self.multi_cell(0, 8, text, 1, 'C', True)
        self.ln(3)
        
    def add_table(self, headers, data, widths=None, header_color=(34, 139, 34)):
        if widths is None:
            widths = [190 // len(headers)] * len(headers)
            
        # Header
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(*header_color)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        # Data rows
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        fill = False
        for row in data:
            if fill:
                self.set_fill_color(245, 255, 245)
            else:
                self.set_fill_color(255, 255, 255)
            for i, cell in enumerate(row):
                self.cell(widths[i], 6, str(cell), 1, 0, 'C', True)
            self.ln()
            fill = not fill
        self.ln(3)
        
    def add_meal_table(self, meal_name, time, protein, calories, foods):
        self.set_font('Helvetica', 'B', 10)
        self.set_fill_color(70, 130, 180)
        self.set_text_color(255, 255, 255)
        self.cell(95, 7, meal_name, 1, 0, 'L', True)
        self.cell(30, 7, time, 1, 0, 'C', True)
        self.cell(30, 7, f'{protein}g protein', 1, 0, 'C', True)
        self.cell(35, 7, f'{calories} kcal', 1, 1, 'C', True)
        
        # Food items
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        headers = ['Food', 'Quantity', 'Protein', 'Calories']
        widths = [70, 50, 35, 35]
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(200, 220, 240)
        for i, header in enumerate(headers):
            self.cell(widths[i], 6, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        for food in foods:
            self.cell(widths[0], 5, food[0], 1, 0, 'L')
            self.cell(widths[1], 5, food[1], 1, 0, 'C')
            self.cell(widths[2], 5, food[2], 1, 0, 'C')
            self.cell(widths[3], 5, food[3], 1, 1, 'C')
        self.ln(3)
        
    def add_text(self, text):
        self.set_font('Helvetica', '', 9)
        self.multi_cell(0, 5, text)
        self.ln(2)
        
    def add_bullet_point(self, text):
        self.set_font('Helvetica', '', 9)
        self.cell(5, 5, chr(149), 0, 0)  # Bullet character
        self.multi_cell(0, 5, text)


def generate_meal_plan_pdf():
    pdf = MealPlanPDF()
    
    # Page 1: Overview and Profile
    pdf.add_page()
    
    pdf.add_section_title('YOUR PROFILE & DAILY TARGETS')
    
    profile_data = [
        ['Current Weight', '95 kg', 'Target Weight', '80 kg'],
        ['Timeline', '11 months', 'Weekly Loss', '0.5-1 kg'],
        ['Daily Calories', '~2,000 kcal', 'Deficit', '20%'],
        ['Daily Protein', '190g (2.0g/kg)', 'Meals', '5-6 per day'],
    ]
    
    pdf.set_font('Helvetica', '', 9)
    for row in profile_data:
        pdf.set_fill_color(240, 255, 240)
        pdf.cell(45, 7, row[0], 1, 0, 'L', True)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(50, 7, row[1], 1, 0, 'C')
        pdf.set_fill_color(240, 255, 240)
        pdf.cell(45, 7, row[2], 1, 0, 'L', True)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(50, 7, row[3], 1, 1, 'C')
    pdf.ln(5)
    
    pdf.add_section_title('EVIDENCE-BASED PRINCIPLES')
    
    principles = [
        ['Protein for Recomposition', '1.6-2.4 g/kg/day', 'Morton et al., 2018'],
        ['Protein per Meal', '0.4-0.6 g/kg', 'Moore et al., 2015'],
        ['Meal Spacing', '3-5 hours apart', 'Areta et al., 2013'],
        ['Pre-Sleep Protein', '30-40g casein', 'Snijders et al., 2015'],
        ['Caloric Deficit', '20-25% below TDEE', 'Longland et al., 2016'],
    ]
    
    pdf.add_table(['Principle', 'Recommendation', 'Research Source'], principles, [70, 50, 70])
    
    pdf.add_section_title('YOUR AVAILABLE FOODS')
    
    foods_text = """PROTEINS: Fish, Chicken, Eggs, Paneer (cottage cheese), Lentils/Dal
VEGETABLES: Broccoli, Beans, Spinach, Green leafy veggies, Cauliflower, Potatoes
FRUITS: Apples, Grapes, Blueberries, Oranges, Tangerines
DAIRY: Milk, Paneer, Curd/Yogurt
SUPPLEMENTS: Whey Protein, Fish Oil 1000mg, Multivitamin, Creatine, BCAAs
BEVERAGES: Green Tea, Indian CTC Milk Tea, Coffee
AVOID: Pork, Beef, Excessive Sugar"""
    
    pdf.add_text(foods_text)
    
    # Page 2: Training Day Meal Plan
    pdf.add_page()
    
    pdf.add_section_title('TRAINING DAY MEAL PLAN', (0, 100, 0))
    pdf.add_info_box('Total: ~2,000 kcal | 190g Protein | 180g Carbs | 65g Fat')
    
    # Meal 1
    pdf.add_meal_table('MEAL 1: Protein-Rich Breakfast', '6:00-7:00 AM', 45, 450, [
        ('Whole Eggs', '3 large', '18g', '210'),
        ('Egg Whites', '3 additional', '11g', '50'),
        ('Spinach (sauteed)', '1 cup', '3g', '40'),
        ('Whole Wheat Toast/Roti', '1 piece', '4g', '80'),
        ('Green Tea', '1 cup', '0g', '5'),
        ('Fish Oil + Multivitamin', '1 each', '0g', '10'),
    ])
    
    # Meal 2
    pdf.add_meal_table('MEAL 2: Mid-Morning Snack', '10:00 AM', 35, 300, [
        ('Paneer (cottage cheese)', '100g', '18g', '260'),
        ('Apple', '1 medium', '0.5g', '95'),
    ])
    
    # Meal 3
    pdf.add_meal_table('MEAL 3: Pre-Workout Lunch', '1:00-2:00 PM', 50, 550, [
        ('Grilled Chicken Breast', '180g', '42g', '280'),
        ('Dal (Lentils)', '1/2 cup', '9g', '115'),
        ('Brown Rice/Chapati', '1/2 cup / 1 roti', '3g', '100'),
        ('Mixed Vegetables', '1 cup', '4g', '80'),
    ])
    
    # Page 3: More meals
    pdf.add_page()
    
    pdf.add_section_title('TRAINING DAY MEALS (Continued)', (0, 100, 0))
    
    # Post-workout
    pdf.add_subsection_title('PERI-WORKOUT NUTRITION (3:00-5:30 PM)')
    peri_workout = [
        ('Pre-Workout Coffee', '1 cup', '0g', '5'),
        ('Water (during)', '500-750ml', '0g', '0'),
        ('BCAA (optional)', '5-10g', '0g', '0'),
        ('Whey Protein Shake', '1 scoop (30g)', '24g', '120'),
        ('Creatine', '5g', '0g', '0'),
        ('Banana (optional)', '1 medium', '1g', '105'),
    ]
    
    pdf.set_font('Helvetica', '', 8)
    headers = ['Item', 'Quantity', 'Protein', 'Calories']
    widths = [70, 50, 35, 35]
    
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(255, 165, 0)
    pdf.set_text_color(255, 255, 255)
    for i, header in enumerate(headers):
        pdf.cell(widths[i], 6, header, 1, 0, 'C', True)
    pdf.ln()
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    for food in peri_workout:
        pdf.cell(widths[0], 5, food[0], 1, 0, 'L')
        pdf.cell(widths[1], 5, food[1], 1, 0, 'C')
        pdf.cell(widths[2], 5, food[2], 1, 0, 'C')
        pdf.cell(widths[3], 5, food[3], 1, 1, 'C')
    pdf.ln(5)
    
    # Meal 4
    pdf.add_meal_table('MEAL 4: Post-Workout Dinner', '7:00-8:00 PM', 45, 380, [
        ('Fish (Salmon/Rohu/Pomfret)', '200g', '40g', '280'),
        ('Steamed Broccoli', '1.5 cups', '5g', '50'),
        ('Cauliflower Rice', '1 cup', '2g', '25'),
        ('Mixed Greens Salad', '1 cup', '2g', '20'),
    ])
    
    # Meal 5
    pdf.add_meal_table('MEAL 5: Pre-Sleep Recovery', '9:30-10:00 PM', 30, 200, [
        ('Warm Milk', '250ml', '8g', '150'),
        ('Whey Protein (1/2 scoop)', '15g', '12g', '60'),
        ('OR Paneer', '80g', '14g', '200'),
    ])
    
    # Daily Summary
    pdf.add_subsection_title('DAILY NUTRITION SUMMARY')
    summary_data = [
        ['Breakfast', '45g', '450 kcal'],
        ['Mid-Morning', '35g', '300 kcal'],
        ['Lunch', '50g', '550 kcal'],
        ['Post-Workout', '25g', '130 kcal'],
        ['Dinner', '45g', '380 kcal'],
        ['Pre-Sleep', '20g', '170 kcal'],
        ['TOTAL', '220g', '1,980 kcal'],
    ]
    pdf.add_table(['Meal', 'Protein', 'Calories'], summary_data, [70, 60, 60])
    
    # Page 4: Rest Day + Supplements
    pdf.add_page()
    
    pdf.add_section_title('REST DAY MEAL PLAN', (100, 100, 100))
    pdf.add_info_box('Total: ~1,800 kcal | 180g Protein | 140g Carbs | 60g Fat', (245, 245, 245))
    
    rest_day_data = [
        ['Breakfast', '7:00 AM', '40g', '400 kcal'],
        ['Mid-Morning', '10:00 AM', '30g', '250 kcal'],
        ['Lunch', '1:00 PM', '45g', '450 kcal'],
        ['Snack', '4:00 PM', '25g', '200 kcal'],
        ['Dinner', '7:00 PM', '40g', '400 kcal'],
        ['Pre-Sleep', '9:30 PM', '30g', '200 kcal'],
        ['TOTAL', '', '210g', '1,900 kcal'],
    ]
    pdf.add_table(['Meal', 'Time', 'Protein', 'Calories'], rest_day_data, [50, 40, 50, 50])
    
    pdf.add_text('Key Differences on Rest Days:\n- Slightly lower calories (no workout expenditure)\n- Lower carbs (less glycogen needed)\n- Same high protein (muscle repair still occurring)')
    
    pdf.add_section_title('SUPPLEMENT TIMING PROTOCOL')
    
    supplement_data = [
        ['Whey Protein', '25-30g', 'Post-workout', 'Rapid MPS stimulation'],
        ['Fish Oil', '1000mg', 'With breakfast', 'Fat-soluble, aids absorption'],
        ['Multivitamin', '1 tablet', 'With breakfast', 'Fat-soluble vitamins need food'],
        ['Creatine', '5g/day', 'Post-workout', 'Slight advantage vs pre-workout'],
        ['BCAA', '5-10g', 'During workout', 'Only if >3h since protein meal'],
        ['Green Tea', '2-3 cups', 'Morning/afternoon', 'Metabolism boost'],
        ['Coffee', '1-2 cups', '30 min pre-workout', 'Performance enhancement'],
    ]
    pdf.add_table(['Supplement', 'Dose', 'Timing', 'Reason'], supplement_data, [40, 30, 45, 75])
    
    # Page 5: Indian Meal Options
    pdf.add_page()
    
    pdf.add_section_title('INDIAN MEAL OPTIONS', (255, 140, 0))
    
    pdf.add_subsection_title('Breakfast Options')
    breakfast_options = [
        ['Egg Bhurji (4 eggs) + toast', '28g protein', '380 kcal'],
        ['Paneer Paratha (light) + curd', '20g protein', '350 kcal'],
        ['Chicken Keema (100g) + roti', '32g protein', '300 kcal'],
    ]
    pdf.add_table(['Option', 'Protein', 'Calories'], breakfast_options, [100, 45, 45])
    
    pdf.add_subsection_title('Lunch Options')
    lunch_options = [
        ['Tandoori Chicken Thali', '52g protein', '550 kcal'],
        ['Fish Curry + brown rice + sabzi', '45g protein', '500 kcal'],
        ['Egg Curry (4 eggs) + 2 chapati', '30g protein', '480 kcal'],
    ]
    pdf.add_table(['Option', 'Protein', 'Calories'], lunch_options, [100, 45, 45])
    
    pdf.add_subsection_title('Dinner Options')
    dinner_options = [
        ['Grilled/Baked Fish + steamed veggies', '42g protein', '350 kcal'],
        ['Palak Paneer (150g) + salad only', '28g protein', '400 kcal'],
        ['Chicken Tikka (200g) + salad', '44g protein', '320 kcal'],
    ]
    pdf.add_table(['Option', 'Protein', 'Calories'], dinner_options, [100, 45, 45])
    
    # Protein Quick Reference
    pdf.add_section_title('PROTEIN QUICK REFERENCE')
    
    protein_ref = [
        ['Chicken Breast', '100g', '31g', 'Lean protein'],
        ['Fish (average)', '100g', '20-25g', 'Omega-3s'],
        ['Eggs', '1 large', '6g', 'Complete protein'],
        ['Egg Whites', '1 large', '3.6g', 'Low calorie'],
        ['Paneer', '100g', '18g', 'Slow-digesting'],
        ['Lentils (dal)', '1 cup cooked', '18g', 'Plant protein'],
        ['Milk', '250ml', '8g', 'Pre-sleep'],
        ['Whey Protein', '1 scoop', '24-25g', 'Fast-digesting'],
        ['Greek Curd', '200g', '20g', 'High protein'],
    ]
    pdf.add_table(['Food', 'Serving', 'Protein', 'Best For'], protein_ref, [50, 40, 40, 60])
    
    # Page 6: Guidelines and Checklist
    pdf.add_page()
    
    pdf.add_section_title('IMPORTANT GUIDELINES')
    
    pdf.add_subsection_title('For Optimal Fat Loss + Muscle Gain:')
    guidelines = [
        "Protein First: Every meal should center around protein",
        "Consistent Intake: Hit 180-200g protein DAILY, no exceptions",
        "Meal Spacing: 3-5 hours between protein meals for optimal MPS",
        "Hydration: 3-4 liters water daily (aids fat metabolism)",
        "Sleep: 7-9 hours critical for muscle recovery and fat loss",
        "Track Progress: Weekly weigh-ins (same time, same conditions)",
    ]
    for g in guidelines:
        pdf.add_bullet_point(g)
    pdf.ln(3)
    
    pdf.add_subsection_title('Signs of Progress:')
    signs = [
        "Clothes fitting differently (even if scale doesn't move)",
        "Strength increasing in workouts",
        "Body measurements changing",
        "0.5-1 kg loss per week on average",
    ]
    for s in signs:
        pdf.add_bullet_point(s)
    pdf.ln(3)
    
    pdf.add_subsection_title('Avoid These Mistakes:')
    pdf.set_text_color(180, 0, 0)
    mistakes = [
        "Skipping protein at any meal",
        "Going more than 5 hours without protein during daytime",
        "Excessive sugar (limit to 25g/day max)",
        "Large caloric deficits (>500 kcal) - muscle loss risk",
        "Alcohol (inhibits MPS and fat oxidation)",
    ]
    for m in mistakes:
        pdf.add_bullet_point(m)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    
    pdf.add_section_title('DAILY CHECKLIST')
    
    pdf.set_font('Helvetica', '', 10)
    checklist = [
        "[ ] Protein Goal: _____/190g",
        "[ ] Water: _____/3.5L",
        "[ ] Meals eaten: ___/5",
        "[ ] Fish Oil taken",
        "[ ] Multivitamin taken",
        "[ ] Creatine taken",
        "[ ] Sleep: _____/8 hours",
        "[ ] Workout completed",
    ]
    for item in checklist:
        pdf.cell(0, 7, item, 0, 1)
    
    pdf.ln(5)
    pdf.add_section_title('HYDRATION TARGETS')
    
    hydration_data = [
        ['Morning (6-10 AM)', '1 liter', '[ ]'],
        ['Midday (10 AM-2 PM)', '750ml', '[ ]'],
        ['Workout (3-5:30 PM)', '750ml', '[ ]'],
        ['Evening (6-10 PM)', '1 liter', '[ ]'],
        ['TOTAL', '3.5 liters', ''],
    ]
    pdf.add_table(['Time', 'Amount', 'Done'], hydration_data, [70, 60, 60])
    
    # Save PDF
    output_path = os.path.join(os.path.dirname(__file__), 'NUTRITION_MEAL_PLAN.pdf')
    pdf.output(output_path)
    print(f"PDF generated successfully: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_meal_plan_pdf()
