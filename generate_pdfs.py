"""
Fitness Tracker PDF Generator (Age 37+ Edition)
Generates Weekly Plan and Daily Exercise Tracker PDFs with injury prevention focus
"""

from fpdf import FPDF
from datetime import datetime, timedelta
import os

class WeeklyPlanPDF(FPDF):
    """Generate a comprehensive weekly plan PDF with warm-up and flexibility focus"""
    
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(30, 60, 114)
        self.cell(0, 10, 'WEEKLY FITNESS PLAN (Age 37+ Safe Edition)', 0, 1, 'C')
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, 'Injury Prevention | Gradual Progression | Flexibility Focus', 0, 1, 'C')
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Generated: {datetime.now().strftime("%Y-%m-%d")}', 0, 0, 'C')
        
    def add_section_title(self, title, color=(30, 60, 114)):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*color)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_text_color(0, 0, 0)
        
    def add_warning_box(self, text):
        self.set_fill_color(255, 243, 205)
        self.set_draw_color(255, 193, 7)
        self.set_font('Helvetica', 'B', 9)
        self.multi_cell(0, 6, text, 1, 'L', True)
        self.ln(3)
        
    def add_info_box(self, text):
        self.set_fill_color(209, 236, 241)
        self.set_draw_color(23, 162, 184)
        self.set_font('Helvetica', '', 9)
        self.multi_cell(0, 6, text, 1, 'L', True)
        self.ln(3)
        
    def create_weekly_plan(self):
        self.add_page()
        
        # Key Rules Section
        self.add_section_title('KEY RULES FOR 37+ TRAINING', (220, 53, 69))
        self.add_warning_box(
            '1. NEVER skip warm-up (15-20 min minimum)\n'
            '2. ALWAYS do flexibility work (morning + evening)\n'
            '3. STOP if you feel sharp pain - not muscle burn\n'
            '4. Progress slowly - max 10% increase per week\n'
            '5. Sleep 7-9 hours - recovery is when you grow'
        )
        
        # Weekly Schedule
        self.add_section_title('WEEKLY SCHEDULE')
        
        schedule = [
            ('Day 1', 'Push (Chest/Shoulders/Triceps)', '2.5 hrs', 'Warm-up + Workout + Stretching'),
            ('Day 2', 'Pull (Back/Biceps) + Flexibility', '2.5 hrs', 'Extended flexibility session'),
            ('Day 3', 'REST + Mobility Work', '30-45 min', 'Light stretching, foam rolling'),
            ('Day 4', 'Legs + Core', '2.5 hrs', 'Critical warm-up for lower body'),
            ('Day 5', 'REST + Light Stretching', '20-30 min', 'Active recovery'),
            ('Day 6', 'Full Body + Mountain Prep', '2.5-3 hrs', 'Hiking/cardio focus'),
            ('Day 7', 'Complete REST', '-', 'Sleep, recover, prepare'),
        ]
        
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(30, 60, 114)
        self.set_text_color(255, 255, 255)
        self.cell(25, 8, 'Day', 1, 0, 'C', True)
        self.cell(55, 8, 'Focus', 1, 0, 'C', True)
        self.cell(25, 8, 'Duration', 1, 0, 'C', True)
        self.cell(85, 8, 'Notes', 1, 1, 'C', True)
        
        self.set_font('Helvetica', '', 9)
        self.set_text_color(0, 0, 0)
        for i, (day, focus, duration, notes) in enumerate(schedule):
            fill = i % 2 == 0
            self.set_fill_color(245, 245, 245) if fill else self.set_fill_color(255, 255, 255)
            self.cell(25, 7, day, 1, 0, 'C', fill)
            self.cell(55, 7, focus, 1, 0, 'L', fill)
            self.cell(25, 7, duration, 1, 0, 'C', fill)
            self.cell(85, 7, notes, 1, 1, 'L', fill)
        
        self.ln(5)
        
        # Warm-Up Protocol
        self.add_section_title('MANDATORY WARM-UP PROTOCOL (15-20 min)')
        self.add_info_box(
            'Upper Body Days: Arm circles, wall slides, cat-cow, band pull-aparts, scapular push-ups, wrist circles\n'
            'Lower Body Days: Light cardio, leg swings, hip circles, glute bridges, monster walks, deep squat holds\n'
            'NEVER SKIP THIS - Your joints need this preparation!'
        )
        
        # Exercise Overview
        self.add_section_title('DAY 1: PUSH EXERCISES')
        push_exercises = [
            ('Flat Bench Press', '4x10-12', '120s', 'Control the weight'),
            ('Incline Dumbbell Press', '3x10-12', '90s', '30-degree incline'),
            ('Overhead Press (seated)', '4x10-12', '120s', 'Strict form'),
            ('Cable Flyes', '3x12-15', '60s', 'Squeeze at top'),
            ('Lateral Raises', '3x12-15', '60s', 'Light weight'),
            ('Tricep Dips (assisted)', '3x10-12', '90s', 'Go to 90 degrees only'),
            ('Overhead Tricep Extension', '3x12-15', '60s', 'Keep elbows in'),
        ]
        self._add_exercise_table(push_exercises)
        
        self.add_page()
        
        self.add_section_title('DAY 2: PULL EXERCISES')
        pull_exercises = [
            ('Pull-ups (assisted if needed)', '4x8-10', '120s', 'Quality over quantity'),
            ('Barbell Rows', '4x10-12', '120s', 'No jerking'),
            ('Single-Arm Dumbbell Row', '3x10-12 each', '90s', 'Full stretch'),
            ('Face Pulls', '3x15-20', '60s', 'Rear delt focus'),
            ('Barbell Curls', '3x10-12', '60s', 'No momentum'),
            ('Hammer Curls', '3x12-15', '60s', 'Forearm development'),
            ('Reverse Grip Curls', '2x15', '60s', 'Wrist health'),
        ]
        self._add_exercise_table(pull_exercises)
        
        self.ln(3)
        
        self.add_section_title('DAY 4: LEGS + CORE')
        leg_exercises = [
            ('Barbell Squats', '4x10-12', '150s', 'Parallel minimum'),
            ('Romanian Deadlift', '4x10-12', '120s', 'Hip hinge pattern'),
            ('Leg Press', '3x12-15', '90s', 'Full range'),
            ('Walking Lunges', '3x12 each', '90s', 'Light dumbbells'),
            ('Leg Curls', '3x12-15', '60s', 'Squeeze at top'),
            ('Calf Raises (seated+standing)', '3+3x15-20', '60s', 'Both variations'),
            ('Hanging Leg Raises', '3x12-15', '60s', 'Core focus'),
        ]
        self._add_exercise_table(leg_exercises)
        
        self.ln(3)
        
        self.add_section_title('DAY 6: FULL BODY + MOUNTAIN PREP')
        full_body = [
            ('Incline Treadmill (15% grade)', '1x30-45 min', '-', 'With light backpack'),
            ('Box Step-ups', '3x15 each', '60s', 'Increase height over time'),
            ('Goblet Squats', '3x20', '60s', 'Endurance focus'),
            ('Single-Leg RDL', '3x12 each', '60s', 'Balance training'),
            ('Walking Lunges', '3x20 each', '60s', 'Continuous'),
            ('Plank to Push-up', '3x12', '60s', 'Core endurance'),
        ]
        self._add_exercise_table(full_body)
        
        # Daily Flexibility
        self.add_page()
        self.add_section_title('DAILY FLEXIBILITY PROTOCOL (NON-NEGOTIABLE)')
        
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, 'Morning Routine (10-15 min) - Do EVERY day', 0, 1)
        morning = [
            ('Cat-cow stretches', '1 min'),
            ('World\'s greatest stretch', '1 min each side'),
            ('Down dog to up dog flow', '1 min'),
            ('Hip circles', '30 sec each direction'),
            ('Shoulder & neck rolls', '1 min'),
            ('Standing quad stretch', '30 sec each'),
            ('Standing hamstring stretch', '30 sec each'),
        ]
        self._add_stretch_table(morning)
        
        self.ln(3)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, 'Evening Routine (15-20 min) - Do on ALL days', 0, 1)
        evening = [
            ('Pigeon pose', '90 sec each side'),
            ('Seated forward fold', '60 sec'),
            ('Supine spinal twist', '60 sec each side'),
            ('Figure-4 stretch', '60 sec each side'),
            ('Hip flexor lunge stretch', '60 sec each side'),
            ('Chest doorway stretch', '45 sec each side'),
            ('Child\'s pose', '60 sec'),
        ]
        self._add_stretch_table(evening)
        
        # Nutrition Quick Reference
        self.ln(5)
        self.add_section_title('NUTRITION QUICK REFERENCE')
        
        nutrition = [
            ('Daily Calories', '2,100-2,300 kcal'),
            ('Protein', '160-180g (key for recovery)'),
            ('Carbs', '180-220g'),
            ('Fats', '60-80g'),
            ('Water', '3-4 liters'),
        ]
        
        self.set_font('Helvetica', '', 10)
        for item, value in nutrition:
            self.cell(60, 7, item + ':', 0, 0, 'L')
            self.set_font('Helvetica', 'B', 10)
            self.cell(0, 7, value, 0, 1, 'L')
            self.set_font('Helvetica', '', 10)
        
        # Joint Support Foods
        self.ln(3)
        self.add_info_box(
            'Joint-Supporting Foods: Fatty fish (omega-3s), bone broth (collagen), berries (antioxidants),\n'
            'turmeric & ginger (anti-inflammatory), leafy greens (vitamins), nuts & seeds (healthy fats)'
        )
        
        # Progress Targets
        self.ln(3)
        self.add_section_title('EXPECTED PROGRESS (Be Patient!)')
        progress = [
            ('Month 1-2', '95kg -> 92kg', 'Build habits, improve mobility'),
            ('Month 3-4', '92kg -> 88kg', 'Strength gains visible'),
            ('Month 5-6', '88kg -> 85kg', 'Muscle definition'),
            ('Month 7-8', '85kg -> 82kg', 'Peak strength phase'),
            ('Month 9-10', '82kg -> 80kg', 'Mountain ready'),
            ('Month 11', '80kg maintain', 'Final preparation'),
        ]
        
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(30, 60, 114)
        self.set_text_color(255, 255, 255)
        self.cell(30, 7, 'Timeline', 1, 0, 'C', True)
        self.cell(40, 7, 'Weight', 1, 0, 'C', True)
        self.cell(120, 7, 'Milestone', 1, 1, 'C', True)
        
        self.set_font('Helvetica', '', 9)
        self.set_text_color(0, 0, 0)
        for timeline, weight, milestone in progress:
            self.cell(30, 6, timeline, 1, 0, 'C')
            self.cell(40, 6, weight, 1, 0, 'C')
            self.cell(120, 6, milestone, 1, 1, 'L')
            
    def _add_exercise_table(self, exercises):
        self.set_font('Helvetica', 'B', 7)
        self.set_fill_color(30, 60, 114)
        self.set_text_color(255, 255, 255)
        self.cell(70, 6, 'Exercise', 1, 0, 'C', True)
        self.cell(25, 6, 'Sets x Reps', 1, 0, 'C', True)
        self.cell(18, 6, 'Rest', 1, 0, 'C', True)
        self.cell(77, 6, 'Notes', 1, 1, 'C', True)
        
        self.set_font('Helvetica', '', 7)
        self.set_text_color(0, 0, 0)
        for i, (exercise, sets_reps, rest, notes) in enumerate(exercises):
            fill = i % 2 == 0
            self.set_fill_color(245, 245, 245) if fill else self.set_fill_color(255, 255, 255)
            self.cell(70, 6, exercise, 1, 0, 'L', fill)
            self.cell(25, 6, sets_reps, 1, 0, 'C', fill)
            self.cell(18, 6, rest, 1, 0, 'C', fill)
            self.cell(77, 6, notes, 1, 1, 'L', fill)
            
    def _add_stretch_table(self, stretches):
        self.set_font('Helvetica', '', 9)
        for stretch, duration in stretches:
            self.cell(80, 6, stretch, 0, 0, 'L')
            self.cell(40, 6, duration, 0, 1, 'L')


class DailyTrackerPDF(FPDF):
    """Generate daily exercise tracking sheets with warm-up and flexibility checkboxes"""
    
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(30, 60, 114)
        self.cell(0, 10, 'DAILY FITNESS TRACKER (Age 37+ Safe Training)', 0, 1, 'C')
        self.ln(2)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
    def add_checkbox(self, label, checked=False):
        box = '[X]' if checked else '[  ]'
        self.cell(8, 5, box, 0, 0, 'L')
        self.cell(0, 5, label, 0, 1, 'L')
        
    def create_daily_tracker(self, weeks=4):
        """Create daily tracking pages for specified number of weeks"""
        
        day_templates = [
            {
                'name': 'Day 1: PUSH (Chest/Shoulders/Triceps)',
                'warmup': [
                    'Light cardio (3 min)',
                    'Arm circles forward & back (30s each)',
                    'Wall slides (10 reps)',
                    'Cat-cow stretches (10 reps)',
                    'Band pull-aparts (15 reps)',
                    'Scapular push-ups (10 reps)',
                    'Wrist circles (20 each way)',
                ],
                'exercises': [
                    ('Flat Bench Press', 4, '10-12'),
                    ('Incline Dumbbell Press', 3, '10-12'),
                    ('Overhead Press (seated)', 4, '10-12'),
                    ('Cable Flyes', 3, '12-15'),
                    ('Lateral Raises', 3, '12-15'),
                    ('Tricep Dips (assisted)', 3, '10-12'),
                    ('Overhead Tricep Extension', 3, '12-15'),
                ],
                'cooldown': [
                    'Chest doorway stretch (45s each)',
                    'Shoulder cross-body stretch (45s each)',
                    'Tricep overhead stretch (30s each)',
                    'Child\'s pose (60s)',
                    'Supine spinal twist (45s each)',
                ]
            },
            {
                'name': 'Day 2: PULL (Back/Biceps) + Flexibility',
                'warmup': [
                    'Light cardio (3 min)',
                    'Band pull-aparts (15 reps)',
                    'Face pulls light (15 reps)',
                    'Arm circles (30s each direction)',
                    'Cat-cow stretches (10 reps)',
                    'Light lat pulldowns (15 reps)',
                    'Shoulder rotations (20 reps)',
                ],
                'exercises': [
                    ('Pull-ups (assisted if needed)', 4, '8-10'),
                    ('Barbell Rows', 4, '10-12'),
                    ('Single-Arm Dumbbell Row', 3, '10-12 each'),
                    ('Face Pulls', 3, '15-20'),
                    ('Barbell Curls', 3, '10-12'),
                    ('Hammer Curls', 3, '12-15'),
                    ('Reverse Grip Curls', 2, '15'),
                ],
                'cooldown': [
                    'Lat stretch (45s each)',
                    'Bicep wall stretch (30s each)',
                    'Chest doorway stretch (45s each)',
                    'Pigeon pose (90s each) - EXTENDED',
                    'Seated forward fold (60s)',
                    'Figure-4 stretch (60s each)',
                    'Child\'s pose (60s)',
                ]
            },
            {
                'name': 'Day 3: REST + MOBILITY',
                'warmup': [],
                'exercises': [],
                'cooldown': [],
                'mobility': [
                    'Foam rolling - upper back (3 min)',
                    'Foam rolling - lats (2 min each)',
                    'Foam rolling - quads (2 min each)',
                    'Foam rolling - IT band (2 min each)',
                    'Cat-cow stretches (2 min)',
                    'World\'s greatest stretch (2 min each)',
                    'Hip circles (1 min each direction)',
                    'Thoracic rotations (2 min)',
                    'Deep squat hold (2 min total)',
                    'Pigeon pose (2 min each)',
                    'Child\'s pose (2 min)',
                    'Light walking (15-20 min)',
                ]
            },
            {
                'name': 'Day 4: LEGS + CORE',
                'warmup': [
                    'Light bike or walking (5 min)',
                    'Leg swings front/back (15 each)',
                    'Leg swings side to side (15 each)',
                    'Hip circles (10 each direction)',
                    'Bodyweight squats (10 slow reps)',
                    'Glute bridges (15 reps)',
                    'Monster walks with band (10 steps each)',
                    'Ankle circles (15 each foot)',
                    'Deep squat holds (3x15 sec)',
                ],
                'exercises': [
                    ('Barbell Squats', 4, '10-12'),
                    ('Romanian Deadlift', 4, '10-12'),
                    ('Leg Press', 3, '12-15'),
                    ('Walking Lunges', 3, '12 each'),
                    ('Leg Curls', 3, '12-15'),
                    ('Calf Raises (seated)', 3, '15-20'),
                    ('Calf Raises (standing)', 3, '15-20'),
                    ('Hanging Leg Raises', 3, '12-15'),
                ],
                'cooldown': [
                    'Standing quad stretch (60s each)',
                    'Standing hamstring stretch (60s each)',
                    'Pigeon pose (90s each)',
                    'Hip flexor lunge stretch (60s each)',
                    'Seated butterfly (60s)',
                    'Frog stretch (60s)',
                    'Calf stretch wall (45s each)',
                    'Child\'s pose (60s)',
                ]
            },
            {
                'name': 'Day 5: REST + LIGHT STRETCHING',
                'warmup': [],
                'exercises': [],
                'cooldown': [],
                'mobility': [
                    'Light walking (20 min)',
                    'Cat-cow stretches (1 min)',
                    'Hip circles (30s each direction)',
                    'Shoulder rolls (30s)',
                    'Standing quad stretch (45s each)',
                    'Standing hamstring stretch (45s each)',
                    'Chest doorway stretch (45s each)',
                    'Child\'s pose (60s)',
                    'Deep breathing / meditation (5 min)',
                ]
            },
            {
                'name': 'Day 6: FULL BODY + MOUNTAIN PREP',
                'warmup': [
                    'Light cardio (5 min)',
                    'Leg swings all directions (10 each)',
                    'Arm circles (30s each direction)',
                    'Hip circles (30s each direction)',
                    'Bodyweight squats (10 reps)',
                    'Glute bridges (15 reps)',
                    'Cat-cow stretches (10 reps)',
                ],
                'exercises': [
                    ('Incline Treadmill (15% grade)', 1, '30-45 min'),
                    ('Box Step-ups', 3, '15 each'),
                    ('Goblet Squats', 3, '20'),
                    ('Single-Leg RDL', 3, '12 each'),
                    ('Walking Lunges', 3, '20 each'),
                    ('Plank to Push-up', 3, '12'),
                    ('Farmer\'s Walks', 3, '40m'),
                ],
                'cooldown': [
                    'Full body stretching routine',
                    'Pigeon pose (90s each)',
                    'Hip flexor stretch (60s each)',
                    'Hamstring stretch (60s each)',
                    'Quad stretch (45s each)',
                    'Calf stretch (45s each)',
                    'Child\'s pose (2 min)',
                ]
            },
            {
                'name': 'Day 7: COMPLETE REST',
                'warmup': [],
                'exercises': [],
                'cooldown': [],
                'rest_activities': [
                    'Sleep 8-9 hours',
                    'Stay hydrated (3-4L water)',
                    'Light walking if desired (optional)',
                    'Evening stretching routine (optional)',
                    'Meal prep for the week',
                    'Mental preparation for next week',
                ]
            }
        ]
        
        for week in range(1, weeks + 1):
            for day_idx, template in enumerate(day_templates):
                self.add_page()
                
                # Week and Date header
                self.set_font('Helvetica', 'B', 12)
                self.set_fill_color(30, 60, 114)
                self.set_text_color(255, 255, 255)
                self.cell(0, 8, f'Week {week} - {template["name"]}', 0, 1, 'C', True)
                self.set_text_color(0, 0, 0)
                
                # Date field
                self.set_font('Helvetica', '', 10)
                self.cell(20, 8, 'Date:', 0, 0)
                self.cell(40, 8, '_____________', 0, 0)
                self.cell(30, 8, 'Weight:', 0, 0)
                self.cell(30, 8, '_______ kg', 0, 0)
                self.cell(25, 8, 'Sleep:', 0, 0)
                self.cell(30, 8, '______ hrs', 0, 1)
                
                self.ln(2)
                
                # Pre-workout checklist
                self.set_font('Helvetica', 'B', 10)
                self.set_fill_color(255, 243, 205)
                self.cell(0, 6, 'PRE-WORKOUT CHECKLIST (Must complete!)', 0, 1, 'L', True)
                self.set_font('Helvetica', '', 9)
                self.add_checkbox('Slept 7+ hours last night?')
                self.add_checkbox('Ate 1-2 hours before?')
                self.add_checkbox('Properly hydrated?')
                self.add_checkbox('No pain or injury concerns?')
                
                self.ln(2)
                
                # Different content based on day type
                if template.get('mobility'):
                    # Rest/Mobility day
                    self.set_font('Helvetica', 'B', 10)
                    self.set_fill_color(209, 236, 241)
                    self.cell(0, 6, 'MOBILITY & RECOVERY ACTIVITIES', 0, 1, 'L', True)
                    self.set_font('Helvetica', '', 9)
                    for activity in template['mobility']:
                        self.add_checkbox(activity)
                        
                elif template.get('rest_activities'):
                    # Complete rest day
                    self.set_font('Helvetica', 'B', 10)
                    self.set_fill_color(200, 230, 200)
                    self.cell(0, 6, 'REST DAY ACTIVITIES', 0, 1, 'L', True)
                    self.set_font('Helvetica', '', 9)
                    for activity in template['rest_activities']:
                        self.add_checkbox(activity)
                        
                else:
                    # Training day
                    # Warm-up section
                    self.set_font('Helvetica', 'B', 10)
                    self.set_fill_color(255, 200, 200)
                    self.cell(0, 6, 'WARM-UP (15-20 min) - DO NOT SKIP!', 0, 1, 'L', True)
                    self.set_font('Helvetica', '', 8)
                    for item in template['warmup']:
                        self.add_checkbox(item)
                    
                    self.ln(2)
                    
                    # Main workout
                    self.set_font('Helvetica', 'B', 10)
                    self.set_fill_color(220, 220, 220)
                    self.cell(0, 6, 'MAIN WORKOUT', 0, 1, 'L', True)
                    
                    # Exercise table header
                    self.set_font('Helvetica', 'B', 7)
                    self.set_fill_color(30, 60, 114)
                    self.set_text_color(255, 255, 255)
                    self.cell(58, 6, 'Exercise', 1, 0, 'C', True)
                    self.cell(12, 6, 'Sets', 1, 0, 'C', True)
                    self.cell(18, 6, 'Target', 1, 0, 'C', True)
                    
                    # Set columns for logging
                    for i in range(1, 5):
                        self.cell(23, 6, f'Set {i}', 1, 0, 'C', True)
                    self.ln()
                    
                    self.set_text_color(0, 0, 0)
                    self.set_font('Helvetica', '', 7)
                    
                    for exercise, sets, reps in template['exercises']:
                        self.cell(58, 12, exercise, 1, 0, 'L')
                        self.cell(12, 12, str(sets), 1, 0, 'C')
                        self.cell(18, 12, reps, 1, 0, 'C')
                        
                        for i in range(4):
                            if i < sets:
                                # Weight/Reps logging box
                                y_pos = self.get_y()
                                self.cell(23, 6, 'Wt:___', 1, 0, 'L')
                                self.set_xy(self.get_x() - 23, y_pos + 6)
                                self.cell(23, 6, 'Rps:__', 1, 0, 'L')
                                self.set_xy(self.get_x(), y_pos)
                            else:
                                self.cell(23, 12, '-', 1, 0, 'C')
                        self.ln()
                    
                    self.ln(2)
                    
                    # Cool-down section
                    self.set_font('Helvetica', 'B', 10)
                    self.set_fill_color(200, 230, 200)
                    self.cell(0, 6, 'COOL-DOWN & STRETCHING (15-20 min)', 0, 1, 'L', True)
                    self.set_font('Helvetica', '', 8)
                    for stretch in template['cooldown']:
                        self.add_checkbox(stretch)
                
                self.ln(2)
                
                # Post-workout section
                self.set_font('Helvetica', 'B', 10)
                self.cell(0, 6, 'POST-WORKOUT', 0, 1, 'L')
                self.set_font('Helvetica', '', 9)
                self.add_checkbox('Cool-down/stretching completed?')
                self.add_checkbox('Post-workout nutrition within 1 hour?')
                self.add_checkbox('Logged all exercises above?')
                
                self.ln(2)
                
                # Daily tracking section
                self.set_font('Helvetica', 'B', 9)
                self.cell(0, 6, 'DAILY TRACKING', 0, 1, 'L')
                
                self.set_font('Helvetica', '', 9)
                self.cell(40, 6, 'Energy Level (1-10):', 0, 0)
                self.cell(20, 6, '______', 0, 0)
                self.cell(40, 6, 'Pain/Discomfort?:', 0, 0)
                self.cell(0, 6, '________________', 0, 1)
                
                self.cell(40, 6, 'Water Intake:', 0, 0)
                self.cell(20, 6, '_____ L', 0, 0)
                self.cell(40, 6, 'Protein (approx):', 0, 0)
                self.cell(0, 6, '_______ g', 0, 1)
                
                # Notes section
                self.ln(2)
                self.set_font('Helvetica', 'B', 9)
                self.cell(0, 6, 'Notes / How do you feel?:', 0, 1)
                self.set_font('Helvetica', '', 9)
                self.cell(0, 5, '_' * 70, 0, 1)
                self.cell(0, 5, '_' * 70, 0, 1)


def main():
    """Generate both PDFs"""
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 50)
    print("FITNESS TRACKER PDF GENERATOR (Age 37+ Edition)")
    print("=" * 50)
    
    # Generate Weekly Plan
    print("\n[1/2] Generating Weekly Plan PDF...")
    weekly = WeeklyPlanPDF()
    weekly.create_weekly_plan()
    weekly_path = os.path.join(output_dir, 'Weekly_Plan.pdf')
    weekly.output(weekly_path)
    print(f"      Saved: {weekly_path}")
    
    # Generate Daily Tracker (4 weeks)
    print("\n[2/2] Generating Daily Exercise Tracker PDF (4 weeks)...")
    tracker = DailyTrackerPDF()
    tracker.create_daily_tracker(weeks=4)
    tracker_path = os.path.join(output_dir, 'Daily_Exercise_Tracker.pdf')
    tracker.output(tracker_path)
    print(f"      Saved: {tracker_path}")
    
    print("\n" + "=" * 50)
    print("SUCCESS! Both PDFs generated.")
    print("=" * 50)
    print("\nFiles created:")
    print(f"  1. Weekly_Plan.pdf - Overview & exercises")
    print(f"  2. Daily_Exercise_Tracker.pdf - 4 weeks of tracking sheets")
    print("\nKey features for 37+ training:")
    print("  - Mandatory warm-up checklists (15-20 min)")
    print("  - Extended cool-down/flexibility sections")
    print("  - Pre-workout safety checklist")
    print("  - Pain tracking in daily logs")
    print("  - Gradual progression focus")
    print("\nPrint and start your safe fitness journey!")


if __name__ == "__main__":
    main()
