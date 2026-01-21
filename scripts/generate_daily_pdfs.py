"""
Daily Exercise PDF Generator
Generates individual PDF files for each day of each week
"""

from fpdf import FPDF
from datetime import datetime
import os


class DailyExercisePDF(FPDF):
    """Generate a PDF for a specific day's exercises"""
    
    def __init__(self, week_num, day_num, day_title):
        super().__init__()
        self.week_num = week_num
        self.day_num = day_num
        self.day_title = day_title
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(30, 60, 114)
        self.cell(0, 10, f'WEEK {self.week_num} - DAY {self.day_num}', 0, 1, 'C')
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, self.day_title, 0, 1, 'C')
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, 'Foundation Phase - Age 37+ Safe Training', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Generated: {datetime.now().strftime("%Y-%m-%d")}', 0, 0, 'C')
        
    def add_section_title(self, title, color=(30, 60, 114)):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(*color)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_text_color(0, 0, 0)
        
    def add_duration_box(self, duration):
        self.set_fill_color(209, 236, 241)
        self.set_draw_color(23, 162, 184)
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 8, f'Total Duration: {duration}', 1, 1, 'C', True)
        self.ln(3)
        
    def add_exercise_table(self, exercises, headers=None):
        if headers is None:
            headers = ['Exercise', 'Sets', 'Reps', 'Rest', 'Notes']
        
        # Calculate column widths
        widths = [60, 15, 25, 20, 70]
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(30, 60, 114)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        for i, exercise in enumerate(exercises):
            fill = i % 2 == 0
            self.set_fill_color(245, 245, 245) if fill else self.set_fill_color(255, 255, 255)
            for j, value in enumerate(exercise):
                align = 'L' if j in [0, 4] else 'C'
                self.cell(widths[j], 6, str(value), 1, 0, align, fill)
            self.ln()
        self.ln(3)
        
    def add_warmup_table(self, warmups):
        widths = [120, 40, 30]
        headers = ['Exercise', 'Duration/Reps', 'Done']
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(255, 193, 7)
        self.set_text_color(0, 0, 0)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        for i, (exercise, duration) in enumerate(warmups):
            fill = i % 2 == 0
            self.set_fill_color(255, 253, 240) if fill else self.set_fill_color(255, 255, 255)
            self.cell(widths[0], 6, exercise, 1, 0, 'L', fill)
            self.cell(widths[1], 6, duration, 1, 0, 'C', fill)
            self.cell(widths[2], 6, '[  ]', 1, 0, 'C', fill)
            self.ln()
        self.ln(3)
        
    def add_stretch_table(self, stretches):
        widths = [100, 40, 50]
        headers = ['Stretch', 'Duration', 'Done']
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(40, 167, 69)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        for i, (stretch, duration) in enumerate(stretches):
            fill = i % 2 == 0
            self.set_fill_color(232, 245, 233) if fill else self.set_fill_color(255, 255, 255)
            self.cell(widths[0], 6, stretch, 1, 0, 'L', fill)
            self.cell(widths[1], 6, duration, 1, 0, 'C', fill)
            self.cell(widths[2], 6, '[  ]', 1, 0, 'C', fill)
            self.ln()
        self.ln(3)
        
    def add_notes_section(self):
        self.add_section_title('Session Notes', (100, 100, 100))
        self.set_font('Helvetica', '', 9)
        
        notes_fields = [
            ('Date:', 50),
            ('Energy Level (1-10):', 30),
            ('Workout Quality (1-10):', 30),
            ('Any Pain/Discomfort:', 100),
            ('Notes:', 100),
        ]
        
        for label, line_width in notes_fields:
            self.cell(50, 7, label, 0, 0, 'L')
            self.cell(line_width, 7, '_' * (line_width // 2), 0, 1, 'L')
            
    def add_checklist(self, items):
        self.set_font('Helvetica', '', 9)
        for item in items:
            self.cell(8, 6, '[  ]', 0, 0, 'L')
            self.cell(0, 6, item, 0, 1, 'L')
        self.ln(3)
        
    def add_recovery_content(self, stretches, tips, activities=None):
        """For rest days"""
        self.add_section_title('Light Stretching Routine', (40, 167, 69))
        self.add_stretch_table(stretches)
        
        self.add_section_title('Recovery Tips', (23, 162, 184))
        self.set_font('Helvetica', '', 9)
        for tip in tips:
            self.cell(5, 6, '*', 0, 0, 'L')
            self.cell(0, 6, tip, 0, 1, 'L')
        self.ln(3)
        
        if activities:
            self.add_section_title('Recommended Activities', (100, 100, 100))
            for activity in activities:
                self.cell(5, 6, '*', 0, 0, 'L')
                self.cell(0, 6, activity, 0, 1, 'L')
            self.ln(3)


def create_week1_day1():
    pdf = DailyExercisePDF(1, 1, 'Upper Body + Core')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Light walking/jogging in place', '3 min'),
        ('Arm circles (forward & back)', '30 sec each'),
        ('Wall slides', '10 reps'),
        ('Cat-cow stretches', '10 reps'),
        ('Thread the needle', '8 each side'),
        ('Band pull-aparts', '15 reps'),
        ('Push-up position holds', '3 x 15 sec'),
        ('Scapular push-ups', '10 reps'),
        ('Light band rows', '15 reps'),
        ('Wrist circles', '20 each'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout', (30, 60, 114))
    exercises = [
        ('Incline Push-ups (hands elevated)', '3', '12-15', '90s', 'Focus on form, full range'),
        ('Band-Assisted Pull-ups/Lat Pulldown', '3', '8-10', '120s', 'Controlled tempo'),
        ('Dumbbell Shoulder Press (seated)', '3', '10-12', '90s', 'Light weight'),
        ('Seated Cable Row', '3', '12-15', '90s', 'Squeeze shoulder blades'),
        ('Dumbbell Curls', '2', '12-15', '60s', 'No swinging'),
        ('Tricep Pushdowns', '2', '12-15', '60s', 'Keep elbows fixed'),
        ('Dead Bug', '3', '10 each', '60s', 'Core stability'),
        ('Bird Dog', '3', '10 each', '60s', 'Lower back health'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Cool-Down & Flexibility (15-20 min)', (40, 167, 69))
    stretches = [
        ('Chest doorway stretch', '45 sec each side'),
        ('Cross-body shoulder stretch', '45 sec each side'),
        ('Tricep overhead stretch', '30 sec each side'),
        ('Lat stretch', '45 sec'),
        ('Child\'s pose', '60 sec'),
        ('Neck stretches', '30 sec each'),
        ('Supine spinal twist', '45 sec each side'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_section_title('Completion Checklist', (100, 100, 100))
    pdf.add_checklist([
        'Warm-up completed',
        'All exercises performed with proper form',
        'Cool-down stretches done',
        'Hydration maintained throughout',
    ])
    
    pdf.add_notes_section()
    return pdf


def create_week1_day2():
    pdf = DailyExercisePDF(1, 2, 'Lower Body + Flexibility')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Walking/light bike', '5 min'),
        ('Leg swings (front/back)', '15 each leg'),
        ('Leg swings (side to side)', '15 each leg'),
        ('Bodyweight squats (partial)', '10 reps'),
        ('Hip circles', '10 each direction'),
        ('Glute bridges', '15 reps'),
        ('Monster walks (band)', '10 steps each'),
        ('Ankle circles', '15 each foot'),
        ('Calf raises (slow)', '15 reps'),
        ('Deep squat holds', '3 x 15 sec'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout', (30, 60, 114))
    exercises = [
        ('Goblet Squats', '3', '12-15', '120s', 'Light DB, depth over weight'),
        ('Romanian Deadlift (dumbbell)', '3', '10-12', '120s', 'Feel hamstring stretch'),
        ('Walking Lunges', '3', '10 each', '90s', 'No weight initially'),
        ('Leg Press', '3', '12-15', '90s', 'Moderate depth'),
        ('Lying Leg Curls', '3', '12-15', '60s', 'Hamstring focus'),
        ('Standing Calf Raises', '3', '15-20', '60s', 'Full range of motion'),
        ('Side Plank', '2', '20-30s each', '60s', 'Hip stability'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Extended Flexibility Session (25-30 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '60 sec each leg'),
        ('Standing hamstring stretch', '60 sec each leg'),
        ('Pigeon pose', '90 sec each side'),
        ('Frog stretch', '60 sec'),
        ('Seated butterfly', '60 sec'),
        ('Figure-4 stretch', '60 sec each side'),
        ('Hip flexor lunge stretch', '60 sec each side'),
        ('Calf stretch (wall)', '45 sec each leg'),
        ('Achilles stretch', '45 sec each leg'),
        ('Supine leg raise', '45 sec each leg'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week1_day3():
    pdf = DailyExercisePDF(1, 3, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('20-30 minutes')
    
    pdf.set_font('Helvetica', 'I', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6, 'Rest days are essential for muscle recovery and growth. Light stretching helps maintain mobility and reduces muscle soreness.')
    pdf.ln(5)
    
    stretches = [
        ('Neck rolls', '30 sec each direction'),
        ('Shoulder rolls', '30 sec each direction'),
        ('Standing side stretch', '30 sec each side'),
        ('Standing forward fold', '45 sec'),
        ('Cat-cow stretches', '10 reps'),
        ('Child\'s pose', '60 sec'),
        ('Hip circles', '10 each direction'),
        ('Gentle quad stretch', '30 sec each leg'),
        ('Gentle calf stretch', '30 sec each leg'),
        ('Deep breathing exercises', '2-3 min'),
    ]
    
    tips = [
        'Hydration: Drink plenty of water throughout the day',
        'Nutrition: Focus on protein intake for muscle repair',
        'Sleep: Aim for 7-9 hours of quality sleep',
        'Movement: Light walking is encouraged (15-20 min)',
        'Foam Rolling: Optional 10-15 min session for tight areas',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    
    pdf.add_section_title('Completion Checklist', (100, 100, 100))
    pdf.add_checklist([
        'Light stretching completed',
        'Adequate hydration (8+ glasses of water)',
        'Nutritious meals consumed',
        'Quality rest/sleep planned',
    ])
    
    pdf.add_notes_section()
    return pdf


def create_week1_day4():
    pdf = DailyExercisePDF(1, 4, 'Full Body Circuit + Cardio')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up (15 minutes)', (255, 152, 0))
    warmups = [
        ('Light cardio (bike, walk, elliptical)', '5 min'),
        ('Arm circles', '30 sec each'),
        ('Leg swings', '10 each leg'),
        ('Bodyweight squats', '10 reps'),
        ('Push-up to downward dog', '5 reps'),
        ('Hip circles', '10 each direction'),
        ('Wrist circles', '15 each'),
        ('Ankle circles', '15 each'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Circuit Training (3 rounds, 2 min rest between)', (30, 60, 114))
    circuit = [
        ('Bodyweight Squats', '-', '15', '-', 'Full depth'),
        ('Push-ups (knee variation if needed)', '-', '10-12', '-', 'Quality reps'),
        ('Dumbbell Rows', '-', '12 each', '-', 'Light weight'),
        ('Step-ups', '-', '10 each', '-', 'Moderate height'),
        ('Plank Hold', '-', '30 sec', '-', 'Engage core'),
        ('Band Pull-Aparts', '-', '15', '-', 'Posture work'),
    ]
    pdf.add_exercise_table(circuit, ['Exercise', 'Sets', 'Reps', 'Rest', 'Notes'])
    
    pdf.add_section_title('Cardio Session (20-30 min)', (220, 53, 69))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Week 1-2: Walk at brisk pace for 20 minutes', 0, 1, 'L')
    pdf.cell(0, 6, 'Heart rate: 100-130 bpm (conversational pace)', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Cool-Down (15 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '30 sec each'),
        ('Standing hamstring stretch', '30 sec each'),
        ('Hip flexor stretch', '30 sec each'),
        ('Chest stretch', '30 sec'),
        ('Lat stretch', '30 sec each'),
        ('Child\'s pose', '60 sec'),
        ('Deep breathing', '2 min'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week1_day5():
    pdf = DailyExercisePDF(1, 5, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('20-30 minutes')
    
    pdf.set_font('Helvetica', 'I', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6, 'Second rest day of the week. Your body is adapting to the new training stimulus. Rest is when growth and recovery happen!')
    pdf.ln(5)
    
    stretches = [
        ('Neck stretches (all directions)', '30 sec each'),
        ('Shoulder shrugs', '15 reps'),
        ('Chest opener stretch', '45 sec'),
        ('Seated spinal twist', '30 sec each side'),
        ('Seated forward fold', '45 sec'),
        ('Butterfly stretch', '45 sec'),
        ('Figure-4 stretch', '30 sec each side'),
        ('Lying knee-to-chest', '30 sec each leg'),
        ('Happy baby pose', '45 sec'),
        ('Corpse pose + deep breathing', '2-3 min'),
    ]
    
    tips = [
        'Continue drinking plenty of water',
        'Include anti-inflammatory foods (berries, leafy greens)',
        'Prioritize quality sleep for muscle repair',
        'Practice mindfulness or meditation',
        'Light 15-20 minute walk is beneficial',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    pdf.add_notes_section()
    return pdf


def create_week1_day6():
    pdf = DailyExercisePDF(1, 6, 'Mobility + Light Cardio')
    pdf.add_page()
    pdf.add_duration_box('1.5-2 hours')
    
    pdf.add_section_title('Light Walking or Cycling (20 min)', (23, 162, 184))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Heart rate: 100-120 bpm | Keep conversation pace', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Foam Rolling - Full Body (15 min)', (255, 152, 0))
    foam_rolling = [
        ('Calves', '90 sec each'),
        ('Hamstrings', '90 sec each'),
        ('Quadriceps', '90 sec each'),
        ('IT Band', '60 sec each'),
        ('Glutes', '90 sec each'),
        ('Upper Back', '2 min'),
        ('Lats', '60 sec each'),
    ]
    pdf.add_warmup_table(foam_rolling)
    
    pdf.add_section_title('Yoga Flow - Sun Salutations (15 min)', (156, 39, 176))
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5, '1. Mountain Pose  2. Upward Salute  3. Forward Fold  4. Half Lift\n5. Plank Pose  6. Chaturanga  7. Upward Dog  8. Downward Dog (5 breaths)\n9. Forward Fold  10. Upward Salute  11. Mountain Pose\n\nRepeat 5-6 times. Move with your breath.')
    pdf.ln(5)
    
    pdf.add_section_title('Static Stretching (15 min)', (40, 167, 69))
    stretches = [
        ('Pigeon pose', '90 sec each side'),
        ('Seated forward fold', '60 sec'),
        ('Reclined spinal twist', '60 sec each side'),
        ('Supine figure-4', '60 sec each side'),
        ('Chest opener on floor', '60 sec'),
        ('Child\'s pose', '90 sec'),
        ('Corpse pose', '2-3 min'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week1_day7():
    pdf = DailyExercisePDF(1, 7, 'Complete Rest')
    pdf.add_page()
    
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 12, 'NO STRUCTURED EXERCISE TODAY', 1, 1, 'C', True)
    pdf.ln(5)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 6, 'Complete rest is essential for: muscle repair and growth, nervous system recovery, mental refreshment, and preventing overtraining.')
    pdf.ln(5)
    
    pdf.add_section_title('Recommended Activities', (23, 162, 184))
    activities = [
        'Gentle walking (casual pace, if desired)',
        'Spend time with family/friends',
        'Read a book or watch favorite shows',
        'Practice meditation or deep breathing',
        'Get extra sleep if needed',
    ]
    pdf.set_font('Helvetica', '', 9)
    for activity in activities:
        pdf.cell(5, 6, '*', 0, 0, 'L')
        pdf.cell(0, 6, activity, 0, 1, 'L')
    pdf.ln(5)
    
    pdf.add_section_title('Weekly Reflection', (100, 100, 100))
    pdf.set_font('Helvetica', '', 9)
    reflection_items = [
        'Completed workout sessions: _____',
        'Total exercise time: _____ hours',
        'Biggest win: _________________________________',
        'Challenge overcome: _________________________________',
        'Goals for next week: _________________________________',
    ]
    for item in reflection_items:
        pdf.cell(0, 7, item, 0, 1, 'L')
    
    pdf.ln(5)
    pdf.add_section_title('Progress Check (End of Week 1)', (30, 60, 114))
    
    # Progress table
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(60, 7, 'Metric', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Start', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Current', 1, 0, 'C', True)
    pdf.cell(50, 7, 'Change', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    metrics = ['Weight', 'Energy Level (1-10)', 'Sleep Quality (1-10)', 'Mood (1-10)', 'Soreness Level (1-10)']
    for i, metric in enumerate(metrics):
        fill = i % 2 == 0
        pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(60, 6, metric, 1, 0, 'L', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(50, 6, '', 1, 1, 'C', fill)
    
    return pdf


# Week 2 functions with progressive exercises
def create_week2_day1():
    pdf = DailyExercisePDF(2, 1, 'Upper Body + Core (Progressive)')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Light walking/jogging in place', '3 min'),
        ('Arm circles (forward & back)', '30 sec each'),
        ('Wall slides', '12 reps'),
        ('Cat-cow stretches', '12 reps'),
        ('Thread the needle', '10 each side'),
        ('Band pull-aparts', '18 reps'),
        ('Push-up position holds', '3 x 20 sec'),
        ('Scapular push-ups', '12 reps'),
        ('Light band rows', '18 reps'),
        ('Wrist circles', '20 each'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout (Week 2: +2 reps or slight weight increase)', (30, 60, 114))
    exercises = [
        ('Incline Push-ups (lower incline)', '3', '15-18', '90s', 'Progress toward floor'),
        ('Band-Assisted Pull-ups/Lat Pulldown', '3', '10-12', '120s', 'Less assistance'),
        ('Dumbbell Shoulder Press (seated)', '3', '12-14', '90s', 'Slight weight increase'),
        ('Seated Cable Row', '3', '14-16', '90s', 'Mind-muscle connection'),
        ('Dumbbell Curls', '3', '12-15', '60s', 'Add 1 set this week'),
        ('Tricep Pushdowns', '3', '12-15', '60s', 'Add 1 set this week'),
        ('Dead Bug', '3', '12 each', '60s', 'Increase reps'),
        ('Bird Dog', '3', '12 each', '60s', 'Increase reps'),
        ('Plank Hold', '2', '30 sec', '60s', 'NEW exercise'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Cool-Down & Flexibility (15-20 min)', (40, 167, 69))
    stretches = [
        ('Chest doorway stretch', '45 sec each side'),
        ('Cross-body shoulder stretch', '45 sec each side'),
        ('Tricep overhead stretch', '30 sec each side'),
        ('Lat stretch', '45 sec'),
        ('Child\'s pose', '60 sec'),
        ('Neck stretches', '30 sec each'),
        ('Supine spinal twist', '45 sec each side'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week2_day2():
    pdf = DailyExercisePDF(2, 2, 'Lower Body + Flexibility (Progressive)')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Walking/light bike', '5 min'),
        ('Leg swings (front/back)', '18 each leg'),
        ('Leg swings (side to side)', '18 each leg'),
        ('Bodyweight squats', '12 reps'),
        ('Hip circles', '12 each direction'),
        ('Glute bridges', '18 reps'),
        ('Monster walks (band)', '12 steps each'),
        ('Ankle circles', '18 each foot'),
        ('Calf raises (slow)', '18 reps'),
        ('Deep squat holds', '3 x 20 sec'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout (Week 2 Progression)', (30, 60, 114))
    exercises = [
        ('Goblet Squats', '3', '14-16', '120s', 'Slightly heavier DB'),
        ('Romanian Deadlift (dumbbell)', '3', '12-14', '120s', 'Increase weight'),
        ('Walking Lunges', '3', '12 each', '90s', 'Add light DBs if ready'),
        ('Leg Press', '3', '14-16', '90s', 'Slight weight increase'),
        ('Lying Leg Curls', '3', '14-16', '60s', 'Focus on contraction'),
        ('Standing Calf Raises', '3', '18-22', '60s', 'Pause at top'),
        ('Side Plank', '3', '25-35s each', '60s', 'Increased duration'),
        ('Glute Bridge Hold', '2', '30 sec', '60s', 'NEW exercise'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Extended Flexibility Session (25-30 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '60 sec each leg'),
        ('Standing hamstring stretch', '60 sec each leg'),
        ('Pigeon pose', '90 sec each side'),
        ('Frog stretch', '75 sec'),
        ('Seated butterfly', '75 sec'),
        ('Figure-4 stretch', '60 sec each side'),
        ('Hip flexor lunge stretch', '75 sec each side'),
        ('Calf stretch (wall)', '45 sec each leg'),
        ('Achilles stretch', '45 sec each leg'),
        ('Supine leg raise', '45 sec each leg'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week2_day3():
    pdf = DailyExercisePDF(2, 3, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('20-30 minutes')
    
    stretches = [
        ('Neck rolls', '30 sec each direction'),
        ('Shoulder rolls', '30 sec each direction'),
        ('Standing side stretch', '30 sec each side'),
        ('Standing forward fold', '45 sec'),
        ('Cat-cow stretches', '12 reps'),
        ('Child\'s pose', '60 sec'),
        ('Hip circles', '12 each direction'),
        ('Gentle quad stretch', '30 sec each leg'),
        ('Gentle calf stretch', '30 sec each leg'),
        ('Deep breathing exercises', '2-3 min'),
    ]
    
    tips = [
        'Hydration: Drink plenty of water',
        'Nutrition: Focus on protein for muscle repair',
        'Sleep: Aim for 7-9 hours of quality sleep',
        'Movement: Light walking encouraged (15-20 min)',
        'Foam Rolling: Optional 10-15 min session',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    pdf.add_notes_section()
    return pdf


def create_week2_day4():
    pdf = DailyExercisePDF(2, 4, 'Full Body Circuit + Cardio (Progressive)')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up (15 minutes)', (255, 152, 0))
    warmups = [
        ('Light cardio', '5 min'),
        ('Arm circles', '30 sec each'),
        ('Leg swings', '12 each leg'),
        ('Bodyweight squats', '12 reps'),
        ('Push-up to downward dog', '6 reps'),
        ('Hip circles', '12 each direction'),
        ('Wrist circles', '15 each'),
        ('Ankle circles', '15 each'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Circuit Training (3 rounds, 90 sec rest)', (30, 60, 114))
    circuit = [
        ('Bodyweight Squats', '-', '18', '-', 'Increase from W1'),
        ('Push-ups (progress from knee)', '-', '12-15', '-', 'Quality reps'),
        ('Dumbbell Rows', '-', '14 each', '-', 'Slight weight increase'),
        ('Step-ups', '-', '12 each', '-', 'Add weight/height'),
        ('Plank Hold', '-', '40 sec', '-', 'Increased duration'),
        ('Band Pull-Aparts', '-', '18', '-', 'Posture work'),
        ('Mountain Climbers', '-', '20 total', '-', 'NEW exercise'),
    ]
    pdf.add_exercise_table(circuit)
    
    pdf.add_section_title('Cardio Session (25-30 min)', (220, 53, 69))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Walk brisk pace: 15 min + Light jog intervals: 5 min + Cool-down walk: 5 min', 0, 1, 'L')
    pdf.cell(0, 6, 'Heart rate: 110-140 bpm', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Cool-Down (15 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '30 sec each'),
        ('Standing hamstring stretch', '30 sec each'),
        ('Hip flexor stretch', '30 sec each'),
        ('Chest stretch', '30 sec'),
        ('Lat stretch', '30 sec each'),
        ('Child\'s pose', '60 sec'),
        ('Deep breathing', '2 min'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week2_day5():
    pdf = DailyExercisePDF(2, 5, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('20-30 minutes')
    
    stretches = [
        ('Neck stretches', '30 sec each'),
        ('Shoulder shrugs', '15 reps'),
        ('Chest opener stretch', '45 sec'),
        ('Seated spinal twist', '30 sec each side'),
        ('Seated forward fold', '45 sec'),
        ('Butterfly stretch', '45 sec'),
        ('Figure-4 stretch', '30 sec each side'),
        ('Lying knee-to-chest', '30 sec each leg'),
        ('Happy baby pose', '45 sec'),
        ('Corpse pose + deep breathing', '2-3 min'),
    ]
    
    tips = [
        'Continue drinking plenty of water',
        'Include anti-inflammatory foods',
        'Prioritize quality sleep',
        'Practice mindfulness',
        'Light 15-20 minute walk',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    pdf.add_notes_section()
    return pdf


def create_week2_day6():
    pdf = DailyExercisePDF(2, 6, 'Mobility + Light Cardio')
    pdf.add_page()
    pdf.add_duration_box('1.5-2 hours')
    
    pdf.add_section_title('Light Walking or Cycling (25 min)', (23, 162, 184))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Heart rate: 100-125 bpm | Slight increase from Week 1', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Foam Rolling - Full Body (15 min)', (255, 152, 0))
    foam_rolling = [
        ('Calves', '90 sec each'),
        ('Hamstrings', '90 sec each'),
        ('Quadriceps', '90 sec each'),
        ('IT Band', '60 sec each'),
        ('Glutes', '90 sec each'),
        ('Upper Back', '2 min'),
        ('Lats', '60 sec each'),
    ]
    pdf.add_warmup_table(foam_rolling)
    
    pdf.add_section_title('Yoga Flow - Sun Salutations (18 min)', (156, 39, 176))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Repeat Sun Salutation A 6-7 times. Move with your breath.', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Static Stretching (15 min)', (40, 167, 69))
    stretches = [
        ('Pigeon pose', '90 sec each side'),
        ('Seated forward fold', '75 sec'),
        ('Reclined spinal twist', '60 sec each side'),
        ('Supine figure-4', '60 sec each side'),
        ('Chest opener on floor', '60 sec'),
        ('Child\'s pose', '90 sec'),
        ('Corpse pose', '2-3 min'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week2_day7():
    pdf = DailyExercisePDF(2, 7, 'Complete Rest')
    pdf.add_page()
    
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 12, 'NO STRUCTURED EXERCISE TODAY', 1, 1, 'C', True)
    pdf.ln(5)
    
    pdf.set_text_color(0, 0, 0)
    pdf.add_section_title('Weekly Reflection - Week 2', (30, 60, 114))
    
    pdf.set_font('Helvetica', '', 9)
    reflection_items = [
        'Completed workout sessions: _____',
        'Total exercise time: _____ hours',
        'Biggest win: _________________________________',
        'Progress from Week 1: _________________________________',
        'Goals for Week 3: _________________________________',
    ]
    for item in reflection_items:
        pdf.cell(0, 7, item, 0, 1, 'L')
    
    pdf.ln(5)
    pdf.add_section_title('Progress Check (End of Week 2)', (30, 60, 114))
    
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 7, 'Metric', 1, 0, 'C', True)
    pdf.cell(35, 7, 'Week 1', 1, 0, 'C', True)
    pdf.cell(35, 7, 'Week 2', 1, 0, 'C', True)
    pdf.cell(70, 7, 'Change', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    metrics = ['Weight', 'Energy Level (1-10)', 'Push-up Reps', 'Squat Reps', 'Cardio Duration']
    for i, metric in enumerate(metrics):
        fill = i % 2 == 0
        pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(50, 6, metric, 1, 0, 'L', fill)
        pdf.cell(35, 6, '', 1, 0, 'C', fill)
        pdf.cell(35, 6, '', 1, 0, 'C', fill)
        pdf.cell(70, 6, '', 1, 1, 'C', fill)
    
    return pdf


# Week 3 functions
def create_week3_day1():
    pdf = DailyExercisePDF(3, 1, 'Upper Body + Core (Progressive)')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Light walking/jogging in place', '3 min'),
        ('Arm circles', '30 sec each'),
        ('Wall slides', '12 reps'),
        ('Cat-cow stretches', '12 reps'),
        ('Thread the needle', '10 each side'),
        ('Band pull-aparts', '20 reps'),
        ('Push-up position holds', '3 x 25 sec'),
        ('Scapular push-ups', '12 reps'),
        ('Light band rows', '20 reps'),
        ('Wrist circles', '20 each'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout (Week 3 Progression)', (30, 60, 114))
    exercises = [
        ('Push-ups (floor or low incline)', '4', '12-15', '90s', 'Progress to floor'),
        ('Pull-ups (less assistance)', '4', '8-12', '120s', 'Increase weight/reduce band'),
        ('Dumbbell Shoulder Press (seated)', '4', '10-12', '90s', 'Weight increase'),
        ('Seated Cable Row', '4', '12-15', '90s', 'Weight increase'),
        ('Dumbbell Curls', '3', '12-15', '60s', 'Controlled tempo'),
        ('Tricep Pushdowns', '3', '12-15', '60s', 'Weight increase'),
        ('Dead Bug', '3', '14 each', '60s', 'Slow and controlled'),
        ('Bird Dog', '3', '14 each', '60s', 'Hold at extension'),
        ('Plank Hold', '3', '40 sec', '60s', 'Increased duration'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Cool-Down & Flexibility (15-20 min)', (40, 167, 69))
    stretches = [
        ('Chest doorway stretch', '45 sec each side'),
        ('Cross-body shoulder stretch', '45 sec each side'),
        ('Tricep overhead stretch', '30 sec each side'),
        ('Lat stretch', '45 sec'),
        ('Child\'s pose', '60 sec'),
        ('Neck stretches', '30 sec each'),
        ('Supine spinal twist', '45 sec each side'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week3_day2():
    pdf = DailyExercisePDF(3, 2, 'Lower Body + Flexibility (Progressive)')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Walking/light bike', '5 min'),
        ('Leg swings (front/back)', '20 each leg'),
        ('Leg swings (side to side)', '20 each leg'),
        ('Bodyweight squats', '15 reps'),
        ('Hip circles', '12 each direction'),
        ('Glute bridges', '20 reps'),
        ('Monster walks (band)', '15 steps each'),
        ('Ankle circles', '20 each foot'),
        ('Calf raises (slow)', '20 reps'),
        ('Deep squat holds', '3 x 25 sec'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout (Week 3 Progression)', (30, 60, 114))
    exercises = [
        ('Goblet Squats', '4', '12-15', '120s', 'Weight increase'),
        ('Romanian Deadlift (dumbbell)', '4', '12-14', '120s', 'Progress weight'),
        ('Walking Lunges (weighted)', '3', '12 each', '90s', 'Light dumbbells'),
        ('Leg Press', '4', '12-15', '90s', 'Weight increase'),
        ('Lying Leg Curls', '3', '14-16', '60s', 'Focus on squeeze'),
        ('Standing Calf Raises', '4', '18-22', '60s', 'Add weight if able'),
        ('Side Plank', '3', '35-40s each', '60s', 'Increased duration'),
        ('Glute Bridge Hold', '3', '35 sec', '60s', 'Single leg variation'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Extended Flexibility Session (25-30 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '60 sec each leg'),
        ('Standing hamstring stretch', '60 sec each leg'),
        ('Pigeon pose', '90 sec each side'),
        ('Frog stretch', '90 sec'),
        ('Seated butterfly', '90 sec'),
        ('Figure-4 stretch', '60 sec each side'),
        ('Hip flexor lunge stretch', '90 sec each side'),
        ('Calf stretch (wall)', '45 sec each leg'),
        ('Achilles stretch', '45 sec each leg'),
        ('Supine leg raise', '60 sec each leg'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week3_day3():
    pdf = DailyExercisePDF(3, 3, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('25-35 minutes')
    
    stretches = [
        ('Neck rolls', '30 sec each direction'),
        ('Shoulder rolls', '30 sec each direction'),
        ('Standing side stretch', '45 sec each side'),
        ('Standing forward fold', '60 sec'),
        ('Cat-cow stretches', '15 reps'),
        ('Child\'s pose', '90 sec'),
        ('Hip circles', '15 each direction'),
        ('Gentle quad stretch', '45 sec each leg'),
        ('Gentle calf stretch', '45 sec each leg'),
        ('Deep breathing exercises', '3-4 min'),
    ]
    
    tips = [
        'Continue drinking plenty of water',
        'Maintain protein intake (1.6-2g per kg body weight)',
        'Prioritize 7-9 hours sleep',
        '20-minute leisurely walk encouraged',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    
    pdf.add_section_title('Optional: Light Foam Rolling (10 min)', (255, 152, 0))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Focus on tight areas: Quadriceps, Hamstrings, Calves, Upper back', 0, 1, 'L')
    
    pdf.add_notes_section()
    return pdf


def create_week3_day4():
    pdf = DailyExercisePDF(3, 4, 'Full Body Circuit + Cardio (Progressive)')
    pdf.add_page()
    pdf.add_duration_box('2-2.5 hours')
    
    pdf.add_section_title('Warm-Up (15 minutes)', (255, 152, 0))
    warmups = [
        ('Light cardio', '5 min'),
        ('Arm circles', '30 sec each'),
        ('Leg swings', '15 each leg'),
        ('Bodyweight squats', '15 reps'),
        ('Push-up to downward dog', '8 reps'),
        ('Hip circles', '15 each direction'),
        ('High knees', '30 sec'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Circuit Training (4 rounds, 90 sec rest)', (30, 60, 114))
    circuit = [
        ('Bodyweight Squats', '-', '20', '-', 'Full depth'),
        ('Push-ups (floor)', '-', '14-16', '-', 'Quality reps'),
        ('Dumbbell Rows', '-', '15 each', '-', 'Moderate weight'),
        ('Step-ups (weighted)', '-', '12 each', '-', 'Add light dumbbells'),
        ('Plank Hold', '-', '45 sec', '-', 'Engage core'),
        ('Band Pull-Aparts', '-', '20', '-', 'Posture work'),
        ('Mountain Climbers', '-', '24 total', '-', 'Controlled pace'),
        ('Burpees (modified)', '-', '6-8', '-', 'NEW exercise'),
    ]
    pdf.add_exercise_table(circuit)
    
    pdf.add_section_title('Cardio Session (25-35 min)', (220, 53, 69))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Warm-up walk: 5 min | Jog/walk intervals: 20 min (1 min jog, 1 min walk)', 0, 1, 'L')
    pdf.cell(0, 6, 'Cool-down walk: 5-10 min | Heart rate: 120-150 bpm', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Cool-Down (15 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '30 sec each'),
        ('Standing hamstring stretch', '30 sec each'),
        ('Hip flexor stretch', '30 sec each'),
        ('Chest stretch', '30 sec'),
        ('Lat stretch', '30 sec each'),
        ('Child\'s pose', '60 sec'),
        ('Deep breathing', '2 min'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week3_day5():
    pdf = DailyExercisePDF(3, 5, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('25-35 minutes')
    
    stretches = [
        ('Neck stretches', '30 sec each'),
        ('Shoulder shrugs', '20 reps'),
        ('Chest opener stretch', '60 sec'),
        ('Seated spinal twist', '45 sec each side'),
        ('Seated forward fold', '60 sec'),
        ('Butterfly stretch', '60 sec'),
        ('Figure-4 stretch', '45 sec each side'),
        ('Lying knee-to-chest', '45 sec each leg'),
        ('Happy baby pose', '60 sec'),
        ('Corpse pose + deep breathing', '3-4 min'),
    ]
    
    tips = [
        'Continue drinking plenty of water',
        'Include anti-inflammatory foods',
        'Prioritize quality sleep',
        'Practice mindfulness',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    
    pdf.add_section_title('Mid-Program Check-in', (23, 162, 184))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, '[  ] Great - progressing well', 0, 1, 'L')
    pdf.cell(0, 6, '[  ] Good - some challenges but managing', 0, 1, 'L')
    pdf.cell(0, 6, '[  ] Struggling - need to adjust', 0, 1, 'L')
    
    pdf.add_notes_section()
    return pdf


def create_week3_day6():
    pdf = DailyExercisePDF(3, 6, 'Mobility + Light Cardio')
    pdf.add_page()
    pdf.add_duration_box('1.5-2 hours')
    
    pdf.add_section_title('Light Walking or Cycling (30 min)', (23, 162, 184))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Heart rate: 100-130 bpm | Include some inclines if walking', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Foam Rolling - Full Body (18 min)', (255, 152, 0))
    foam_rolling = [
        ('Calves', '2 min each'),
        ('Hamstrings', '2 min each'),
        ('Quadriceps', '2 min each'),
        ('IT Band', '90 sec each'),
        ('Glutes', '2 min each'),
        ('Upper Back', '2 min'),
        ('Lats', '90 sec each'),
    ]
    pdf.add_warmup_table(foam_rolling)
    
    pdf.add_section_title('Yoga Flow - Sun Salutations A + B (20 min)', (156, 39, 176))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, '8-10 total rounds mixing Sun Salutation A and B with Warrior poses', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Static Stretching (18 min)', (40, 167, 69))
    stretches = [
        ('Pigeon pose', '2 min each side'),
        ('Seated forward fold', '90 sec'),
        ('Reclined spinal twist', '75 sec each side'),
        ('Supine figure-4', '75 sec each side'),
        ('Frog stretch', '90 sec'),
        ('Child\'s pose', '2 min'),
        ('Corpse pose', '3 min'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week3_day7():
    pdf = DailyExercisePDF(3, 7, 'Complete Rest')
    pdf.add_page()
    
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 12, 'NO STRUCTURED EXERCISE TODAY', 1, 1, 'C', True)
    pdf.ln(5)
    
    pdf.set_text_color(0, 0, 0)
    pdf.add_section_title('Weekly Reflection - Week 3', (30, 60, 114))
    
    pdf.set_font('Helvetica', '', 9)
    reflection_items = [
        'Completed workout sessions: _____',
        'Total exercise time: _____ hours',
        'Biggest win: _________________________________',
        'Notable improvements: _________________________________',
        'Goals for Week 4 (Final Foundation Week): _________________________________',
    ]
    for item in reflection_items:
        pdf.cell(0, 7, item, 0, 1, 'L')
    
    pdf.ln(5)
    pdf.add_section_title('Progress Check (End of Week 3)', (30, 60, 114))
    
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(40, 7, 'Metric', 1, 0, 'C', True)
    pdf.cell(30, 7, 'Week 1', 1, 0, 'C', True)
    pdf.cell(30, 7, 'Week 2', 1, 0, 'C', True)
    pdf.cell(30, 7, 'Week 3', 1, 0, 'C', True)
    pdf.cell(60, 7, 'Change', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    metrics = ['Weight', 'Push-up Reps', 'Squat Reps', 'Plank Hold Time', 'Cardio Duration']
    for i, metric in enumerate(metrics):
        fill = i % 2 == 0
        pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(40, 6, metric, 1, 0, 'L', fill)
        pdf.cell(30, 6, '', 1, 0, 'C', fill)
        pdf.cell(30, 6, '', 1, 0, 'C', fill)
        pdf.cell(30, 6, '', 1, 0, 'C', fill)
        pdf.cell(60, 6, '', 1, 1, 'C', fill)
    
    pdf.ln(5)
    pdf.add_section_title('Week 4 Preview', (220, 53, 69))
    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 6, 'Week 4 is the final week of the Foundation Phase. You\'ll test your progress with higher intensity and prepare your body for Phase 2 (Building).')
    
    return pdf


# Week 4 functions (Testing week)
def create_week4_day1():
    pdf = DailyExercisePDF(4, 1, 'Upper Body + Core (TESTING)')
    pdf.add_page()
    pdf.add_duration_box('2.5 hours')
    
    pdf.set_fill_color(220, 53, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 8, 'FINAL WEEK - Test Your Progress!', 1, 1, 'C', True)
    pdf.ln(3)
    pdf.set_text_color(0, 0, 0)
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Light walking/jogging in place', '4 min'),
        ('Arm circles', '30 sec each'),
        ('Wall slides', '15 reps'),
        ('Cat-cow stretches', '15 reps'),
        ('Thread the needle', '12 each side'),
        ('Band pull-aparts', '25 reps'),
        ('Push-up position holds', '3 x 30 sec'),
        ('Scapular push-ups', '15 reps'),
        ('Light band rows', '25 reps'),
        ('Wrist circles', '25 each'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout (Week 4 - Intensity Test)', (30, 60, 114))
    exercises = [
        ('Push-ups (floor)', '4', 'AMRAP*', '120s', 'Record your max!'),
        ('Pull-ups (minimal assistance)', '4', 'AMRAP*', '150s', 'Record your max!'),
        ('Dumbbell Shoulder Press', '4', '10-12', '90s', 'Heaviest with good form'),
        ('Seated Cable Row', '4', '12-15', '90s', 'Weight increase'),
        ('Dumbbell Curls', '3', '10-12', '60s', 'Increase weight'),
        ('Tricep Dips (bench)', '3', '12-15', '60s', 'Upgrade from pushdowns'),
        ('Dead Bug', '3', '15 each', '60s', 'Slow and controlled'),
        ('Bird Dog with Hold', '3', '12 each', '60s', '3 sec hold'),
        ('Plank Hold', '3', 'AMRAP*', '60s', 'Record max time!'),
    ]
    pdf.add_exercise_table(exercises)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(0, 5, '*AMRAP = As Many Reps As Possible', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Progress Test - Record Your Results!', (40, 167, 69))
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(60, 7, 'Exercise', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Week 1', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Week 4', 1, 0, 'C', True)
    pdf.cell(50, 7, 'Improvement', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    tests = ['Push-ups (max reps)', 'Pull-ups (max reps)', 'Plank Hold (max time)', 'Shoulder Press Weight']
    for i, test in enumerate(tests):
        fill = i % 2 == 0
        pdf.set_fill_color(232, 245, 233) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(60, 6, test, 1, 0, 'L', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(50, 6, '', 1, 1, 'C', fill)
    
    pdf.add_notes_section()
    return pdf


def create_week4_day2():
    pdf = DailyExercisePDF(4, 2, 'Lower Body + Flexibility (TESTING)')
    pdf.add_page()
    pdf.add_duration_box('2.5 hours')
    
    pdf.set_fill_color(220, 53, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 8, 'Test Your Lower Body Progress!', 1, 1, 'C', True)
    pdf.ln(3)
    pdf.set_text_color(0, 0, 0)
    
    pdf.add_section_title('Warm-Up Protocol (20 minutes)', (255, 152, 0))
    warmups = [
        ('Walking/light bike', '5 min'),
        ('Leg swings (front/back)', '20 each leg'),
        ('Leg swings (side to side)', '20 each leg'),
        ('Bodyweight squats', '20 reps'),
        ('Hip circles', '15 each direction'),
        ('Glute bridges', '25 reps'),
        ('Monster walks (band)', '15 steps each'),
        ('Ankle circles', '20 each foot'),
        ('Calf raises (slow)', '20 reps'),
        ('Deep squat holds', '3 x 30 sec'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Main Workout (Week 4 - Intensity Test)', (30, 60, 114))
    exercises = [
        ('Goblet Squats', '4', '15-20', '120s', 'Heaviest weight possible'),
        ('Romanian Deadlift (dumbbell)', '4', '12-15', '120s', 'Weight increase'),
        ('Walking Lunges (weighted)', '3', '15 each', '90s', 'Moderate dumbbells'),
        ('Leg Press', '4', '15-18', '90s', 'Test your max'),
        ('Lying Leg Curls', '4', '15-18', '60s', 'Weight increase'),
        ('Standing Calf Raises', '4', '20-25', '60s', 'Full range'),
        ('Bodyweight Squats', '1', 'AMRAP 2min', '-', 'Record total reps!'),
        ('Wall Sit', '3', 'AMRAP', '60s', 'Record max time!'),
    ]
    pdf.add_exercise_table(exercises)
    
    pdf.add_section_title('Progress Test - Record Your Results!', (40, 167, 69))
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(60, 7, 'Exercise', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Week 1', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Week 4', 1, 0, 'C', True)
    pdf.cell(50, 7, 'Improvement', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    tests = ['Goblet Squat Weight', 'Bodyweight Squats (2 min)', 'Wall Sit (max time)', 'Deep Squat Hold']
    for i, test in enumerate(tests):
        fill = i % 2 == 0
        pdf.set_fill_color(232, 245, 233) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(60, 6, test, 1, 0, 'L', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(50, 6, '', 1, 1, 'C', fill)
    
    pdf.ln(3)
    pdf.add_section_title('Extended Flexibility Session (30 min)', (40, 167, 69))
    stretches = [
        ('Standing quad stretch', '75 sec each leg'),
        ('Standing hamstring stretch', '75 sec each leg'),
        ('Pigeon pose', '2 min each side'),
        ('Frog stretch', '90 sec'),
        ('Seated butterfly', '90 sec'),
        ('Figure-4 stretch', '75 sec each side'),
        ('Hip flexor lunge stretch', '90 sec each side'),
        ('Calf stretch (wall)', '60 sec each leg'),
        ('Full forward fold', '90 sec - TEST!'),
    ]
    pdf.add_stretch_table(stretches)
    
    pdf.add_notes_section()
    return pdf


def create_week4_day3():
    pdf = DailyExercisePDF(4, 3, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('30 minutes')
    
    pdf.set_font('Helvetica', 'I', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6, 'Recovery before the final push of Phase 1. Your body needs this rest to consolidate gains from the testing sessions.')
    pdf.ln(5)
    
    stretches = [
        ('Neck rolls', '30 sec each direction'),
        ('Shoulder rolls', '30 sec each direction'),
        ('Standing side stretch', '45 sec each side'),
        ('Standing forward fold', '60 sec'),
        ('Cat-cow stretches', '15 reps'),
        ('Child\'s pose', '90 sec'),
        ('Hip circles', '15 each direction'),
        ('Gentle quad stretch', '45 sec each leg'),
        ('Gentle calf stretch', '45 sec each leg'),
        ('Deep breathing exercises', '4 min'),
    ]
    
    tips = [
        'Extra water today (muscles need it after testing)',
        'Slightly higher protein for recovery',
        'Aim for 8+ hours sleep',
        'Light 20-minute walk is beneficial',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    
    pdf.add_section_title('Optional: Foam Rolling (15 min)', (255, 152, 0))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Focus on: Quadriceps, Hamstrings, Glutes, Upper back', 0, 1, 'L')
    
    pdf.add_notes_section()
    return pdf


def create_week4_day4():
    pdf = DailyExercisePDF(4, 4, 'Full Body Circuit + Cardio (TESTING)')
    pdf.add_page()
    pdf.add_duration_box('2.5-3 hours')
    
    pdf.set_fill_color(220, 53, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 8, 'Test Your Circuit Endurance & Cardio Progress!', 1, 1, 'C', True)
    pdf.ln(3)
    pdf.set_text_color(0, 0, 0)
    
    pdf.add_section_title('Warm-Up (15 minutes)', (255, 152, 0))
    warmups = [
        ('Light cardio', '5 min'),
        ('Arm circles', '30 sec each'),
        ('Leg swings', '15 each leg'),
        ('Bodyweight squats', '15 reps'),
        ('Push-up to downward dog', '10 reps'),
        ('Hip circles', '15 each direction'),
        ('High knees', '45 sec'),
        ('Jumping jacks', '30 sec'),
    ]
    pdf.add_warmup_table(warmups)
    
    pdf.add_section_title('Circuit Training (4 rounds, 60 sec rest)', (30, 60, 114))
    circuit = [
        ('Bodyweight Squats', '-', '25', '-', 'Push yourself!'),
        ('Push-ups (floor)', '-', '15-20', '-', 'Quality reps'),
        ('Dumbbell Rows', '-', '15 each', '-', 'Moderate-heavy'),
        ('Step-ups (weighted)', '-', '15 each', '-', 'Moderate dumbbells'),
        ('Plank Hold', '-', '50 sec', '-', 'Strong core'),
        ('Band Pull-Aparts', '-', '25', '-', 'Posture work'),
        ('Mountain Climbers', '-', '30 total', '-', 'Controlled'),
        ('Burpees', '-', '10', '-', 'Full movement'),
    ]
    pdf.add_exercise_table(circuit)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 6, 'RECORD YOUR TOTAL CIRCUIT TIME: ____________', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Cardio Test (30-40 min)', (220, 53, 69))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Warm-up walk: 3 min | Continuous jog: See how long you can go!', 0, 1, 'L')
    pdf.cell(0, 6, 'Walk breaks as needed | Goal: 15-20 min jogging', 0, 1, 'L')
    pdf.ln(2)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 6, 'Total jogging time: _____ | Longest continuous jog: _____', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Progress Test - Record Your Results!', (40, 167, 69))
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(60, 7, 'Metric', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Week 1', 1, 0, 'C', True)
    pdf.cell(40, 7, 'Week 4', 1, 0, 'C', True)
    pdf.cell(50, 7, 'Improvement', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    tests = ['Circuit Completion Time', 'Continuous Jog Time', 'Total Cardio Duration', 'Rest Between Rounds']
    for i, test in enumerate(tests):
        fill = i % 2 == 0
        pdf.set_fill_color(232, 245, 233) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(60, 6, test, 1, 0, 'L', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(40, 6, '', 1, 0, 'C', fill)
        pdf.cell(50, 6, '', 1, 1, 'C', fill)
    
    pdf.add_notes_section()
    return pdf


def create_week4_day5():
    pdf = DailyExercisePDF(4, 5, 'Rest + Light Stretching')
    pdf.add_page()
    pdf.add_duration_box('30 minutes')
    
    pdf.set_font('Helvetica', 'I', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6, 'Rest before the final mobility session of Phase 1. You\'ve worked hard this week!')
    pdf.ln(5)
    
    stretches = [
        ('Neck stretches', '30 sec each'),
        ('Shoulder shrugs', '20 reps'),
        ('Chest opener stretch', '60 sec'),
        ('Seated spinal twist', '45 sec each side'),
        ('Seated forward fold', '60 sec'),
        ('Butterfly stretch', '60 sec'),
        ('Figure-4 stretch', '45 sec each side'),
        ('Lying knee-to-chest', '45 sec each leg'),
        ('Happy baby pose', '60 sec'),
        ('Corpse pose + deep breathing', '4 min'),
    ]
    
    tips = [
        'Continue drinking plenty of water',
        'Reflect on your 4-week journey',
        'Prioritize quality sleep',
        'Get ready for Phase 2!',
    ]
    
    pdf.add_recovery_content(stretches, tips)
    
    pdf.add_section_title('Reflection Questions', (23, 162, 184))
    pdf.set_font('Helvetica', '', 9)
    questions = [
        'What was the hardest workout this week? _______________',
        'What exercise improved the most? _______________',
        'How has your energy changed? _______________',
        'What are you most proud of? _______________',
    ]
    for q in questions:
        pdf.cell(0, 7, q, 0, 1, 'L')
    
    pdf.add_notes_section()
    return pdf


def create_week4_day6():
    pdf = DailyExercisePDF(4, 6, 'Mobility + Light Cardio (Final Session)')
    pdf.add_page()
    pdf.add_duration_box('2 hours')
    
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 8, 'Final Mobility Assessment - Phase 1', 1, 1, 'C', True)
    pdf.ln(3)
    pdf.set_text_color(0, 0, 0)
    
    pdf.add_section_title('Light Walking or Cycling (35 min)', (23, 162, 184))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, 'Heart rate: 100-130 bpm | Include varied terrain', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Foam Rolling - Full Body (20 min)', (255, 152, 0))
    foam_rolling = [
        ('Calves', '2 min each'),
        ('Hamstrings', '2 min each'),
        ('Quadriceps', '2 min each'),
        ('IT Band', '2 min each'),
        ('Glutes', '2 min each'),
        ('Upper Back', '3 min'),
        ('Lats', '2 min each'),
    ]
    pdf.add_warmup_table(foam_rolling)
    
    pdf.add_section_title('Yoga Flow - Extended Session (25 min)', (156, 39, 176))
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 6, '10 rounds mixing Sun Salutation A & B with Warrior I, II, Triangle pose', 0, 1, 'L')
    pdf.ln(3)
    
    pdf.add_section_title('Flexibility Test & Static Stretching (20 min)', (40, 167, 69))
    
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(70, 7, 'Stretch', 1, 0, 'C', True)
    pdf.cell(35, 7, 'Duration', 1, 0, 'C', True)
    pdf.cell(30, 7, 'Week 1', 1, 0, 'C', True)
    pdf.cell(30, 7, 'Week 4', 1, 0, 'C', True)
    pdf.cell(25, 7, 'Done', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    stretches = [
        ('Pigeon pose', '2 min each'),
        ('Seated forward fold', '2 min'),
        ('Reclined spinal twist', '90 sec each'),
        ('Frog stretch', '90 sec'),
        ('Hip flexor stretch', '90 sec each'),
        ('Shoulder stretch', '60 sec each'),
        ('Child\'s pose', '2 min'),
    ]
    for i, (stretch, duration) in enumerate(stretches):
        fill = i % 2 == 0
        pdf.set_fill_color(232, 245, 233) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(70, 6, stretch, 1, 0, 'L', fill)
        pdf.cell(35, 6, duration, 1, 0, 'C', fill)
        pdf.cell(30, 6, '/10', 1, 0, 'C', fill)
        pdf.cell(30, 6, '/10', 1, 0, 'C', fill)
        pdf.cell(25, 6, '[  ]', 1, 1, 'C', fill)
    
    pdf.add_notes_section()
    return pdf


def create_week4_day7():
    pdf = DailyExercisePDF(4, 7, 'Complete Rest - PHASE 1 COMPLETE!')
    pdf.add_page()
    
    pdf.set_fill_color(40, 167, 69)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 15, 'CONGRATULATIONS!', 1, 1, 'C', True)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, 'Phase 1: Foundation Complete!', 1, 1, 'C', True)
    pdf.ln(5)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 6, 'You have successfully completed Phase 1 of your Ultimate Transformation Plan! You\'ve established proper movement patterns, built foundational strength, improved flexibility, and developed sustainable habits.')
    pdf.ln(5)
    
    pdf.add_section_title('Complete Phase 1 Assessment', (30, 60, 114))
    
    # Strength Progress Table
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 7, 'Strength Progress:', 0, 1, 'L')
    
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 6, 'Exercise', 1, 0, 'C', True)
    pdf.cell(35, 6, 'Week 1', 1, 0, 'C', True)
    pdf.cell(35, 6, 'Week 4', 1, 0, 'C', True)
    pdf.cell(70, 6, '% Improvement', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    exercises = ['Push-ups (max)', 'Pull-ups (max)', 'Bodyweight Squats', 'Plank Hold (max)', 'Wall Sit (max)']
    for i, ex in enumerate(exercises):
        fill = i % 2 == 0
        pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(50, 5, ex, 1, 0, 'L', fill)
        pdf.cell(35, 5, '', 1, 0, 'C', fill)
        pdf.cell(35, 5, '', 1, 0, 'C', fill)
        pdf.cell(70, 5, '', 1, 1, 'C', fill)
    
    pdf.ln(3)
    
    # Cardio Progress
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(0, 7, 'Cardio Progress:', 0, 1, 'L')
    
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(60, 6, 'Metric', 1, 0, 'C', True)
    pdf.cell(40, 6, 'Week 1', 1, 0, 'C', True)
    pdf.cell(40, 6, 'Week 4', 1, 0, 'C', True)
    pdf.cell(50, 6, 'Improvement', 1, 1, 'C', True)
    
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(0, 0, 0)
    cardio = ['Continuous Jog Time', 'Total Cardio Duration', 'Recovery Time']
    for i, c in enumerate(cardio):
        fill = i % 2 == 0
        pdf.set_fill_color(245, 245, 245) if fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(60, 5, c, 1, 0, 'L', fill)
        pdf.cell(40, 5, '', 1, 0, 'C', fill)
        pdf.cell(40, 5, '', 1, 0, 'C', fill)
        pdf.cell(50, 5, '', 1, 1, 'C', fill)
    
    pdf.ln(3)
    
    pdf.add_section_title('Phase 1 Final Reflection', (100, 100, 100))
    pdf.set_font('Helvetica', '', 9)
    reflections = [
        'What worked well? _________________________________',
        'What was challenging? _________________________________',
        'What will you do differently in Phase 2? _________________________________',
    ]
    for r in reflections:
        pdf.cell(0, 7, r, 0, 1, 'L')
    
    pdf.ln(5)
    pdf.add_section_title('Phase 2 Preview: Building (Weeks 5-14)', (220, 53, 69))
    pdf.set_font('Helvetica', '', 9)
    preview = [
        '* Push/Pull/Legs split training',
        '* Weights increase 5-10%',
        '* Cardio extends to 30-45 minutes',
        '* Introduction of barbell exercises',
        '* Mountain-specific training begins',
    ]
    for p in preview:
        pdf.cell(0, 6, p, 0, 1, 'L')
    
    pdf.ln(3)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, 'SEE YOU IN PHASE 2!', 1, 1, 'C', True)
    
    return pdf


def generate_all_pdfs():
    """Generate all PDF files for weeks 1-4"""
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Week 1
    week1_creators = [
        create_week1_day1, create_week1_day2, create_week1_day3,
        create_week1_day4, create_week1_day5, create_week1_day6, create_week1_day7
    ]
    
    # Week 2
    week2_creators = [
        create_week2_day1, create_week2_day2, create_week2_day3,
        create_week2_day4, create_week2_day5, create_week2_day6, create_week2_day7
    ]
    
    # Week 3
    week3_creators = [
        create_week3_day1, create_week3_day2, create_week3_day3,
        create_week3_day4, create_week3_day5, create_week3_day6, create_week3_day7
    ]
    
    # Week 4
    week4_creators = [
        create_week4_day1, create_week4_day2, create_week4_day3,
        create_week4_day4, create_week4_day5, create_week4_day6, create_week4_day7
    ]
    
    all_weeks = [
        (1, week1_creators),
        (2, week2_creators),
        (3, week3_creators),
        (4, week4_creators),
    ]
    
    for week_num, creators in all_weeks:
        week_folder = os.path.join(base_path, f'Week_{week_num}')
        os.makedirs(week_folder, exist_ok=True)
        
        for day_num, creator in enumerate(creators, 1):
            day_folder = os.path.join(week_folder, f'Day_{day_num}')
            os.makedirs(day_folder, exist_ok=True)
            
            pdf = creator()
            pdf_path = os.path.join(day_folder, 'exercises.pdf')
            pdf.output(pdf_path)
            print(f'Generated: Week {week_num} Day {day_num} - {pdf_path}')
            
            # Remove the markdown file if it exists
            md_path = os.path.join(day_folder, 'exercises.md')
            if os.path.exists(md_path):
                os.remove(md_path)
                print(f'Removed: {md_path}')
    
    print('\nAll PDFs generated successfully!')


if __name__ == '__main__':
    generate_all_pdfs()
