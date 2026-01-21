"""
EVIDENCE-BASED WORKOUT PDF GENERATOR v2.0
==========================================
OPTIMIZED FOR: Body Recomposition (Fat Loss + Muscle Preservation)

Based on scientific research from:
- NCBI/PMC5684266: Meta-Analysis on Weekly Set Volume & Strength Gain (2017)
- NCBI/PubMed: Maximizing Muscle Hypertrophy (2019)
- Stronger By Science: Warm-up protocols & Training for Older Lifters
- ACSM Position Stand on Resistance Training for Adults
- Examine.com: Muscle Size & Strength research

==========================================
PROFILE (UPDATED):
==========================================
- Age: 38 years (late 30s considerations applied)
- Height: 180 cm
- Current Weight: 95 kg
- Target Weight: 80 kg (-15 kg body recomposition goal)
- Current BMI: 29.3 (Overweight) -> Target BMI: 24.7 (Normal)
- Training Days: 4 days/week
- Session Duration: 2-3 hours
- Caloric Deficit: 500-700 kcal/day for sustainable fat loss

==========================================
AGE 38 SPECIFIC CONSIDERATIONS:
==========================================
- Testosterone optimization: Compound movements prioritized
- Joint health: Controlled tempo, proper warm-up extended
- Recovery: 48-72 hours between same muscle groups
- Injury prevention: Progressive overload more conservative
- Sleep: 7-9 hours critical for hormone regulation

==========================================
KEY PRINCIPLES APPLIED (META-ANALYSIS BASED):
==========================================
1. VOLUME: Medium-High Weekly Sets (MWS: 5-9 / HWS: 10+) per muscle
   - Meta-analysis shows MWS/HWS produces 15-23% greater strength gains
   - Target: 12-20 working sets/muscle group/week
   
2. INTENSITY: 65-80% 1RM with 6-12 reps for hypertrophy
   - Higher intensity (75-85%) for compound lifts
   - Moderate intensity (65-75%) for isolation

3. PROGRESSIVE OVERLOAD: Conservative 2.5% weekly increase
   - Age 38 requires slower progression to prevent injury
   - Deload every 4th week (this program = build weeks)
   
4. REST INTERVALS (age-adjusted):
   - Compound movements: 2-3 minutes (full ATP recovery)
   - Isolation movements: 60-90 seconds (metabolic stress)
   
5. TEMPO: 2-1-2 (2s eccentric, 1s pause, 2s concentric)
   - Slower tempo for joint protection at 38
   
6. PRE-WORKOUT: Extended warm-up (30-40 min)
   - Joint mobilization before pushing volume
   
7. POST-WORKOUT: LISS cardio (3KM total walking)
   - Fat oxidation in post-workout window
   - NEAT contribution to caloric deficit
   
8. BODY RECOMPOSITION FOCUS:
   - High protein intake (1.8-2.2g/kg = 170-210g/day)
   - Caloric deficit of 500-700 kcal/day
   - Compound movements to preserve muscle in deficit
"""

from fpdf import FPDF
from datetime import datetime
import os


class EnhancedWorkoutPDF(FPDF):
    """Generate evidence-based workout PDFs"""
    
    def __init__(self, week_num, day_num, day_title, focus_area):
        super().__init__()
        self.week_num = week_num
        self.day_num = day_num
        self.day_title = day_title
        self.focus_area = focus_area
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(30, 60, 114)
        self.cell(0, 10, f'WEEK {self.week_num} - DAY {self.day_num}', 0, 1, 'C')
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(220, 53, 69)
        self.cell(0, 8, self.day_title, 0, 1, 'C')
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, f'{self.focus_area} | Age 38 Optimized | Body Recomposition (95kg -> 80kg)', 0, 1, 'C')
        self.ln(3)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | Total Duration: 2-3 Hours | {datetime.now().strftime("%Y-%m-%d")}', 0, 0, 'C')
        
    def add_section_title(self, title, color=(30, 60, 114)):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(*color)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_draw_color(*color)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)
        self.set_text_color(0, 0, 0)
        
    def add_duration_box(self, pre_workout, main_workout, post_workout):
        self.set_fill_color(40, 167, 69)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 10)
        self.cell(63, 8, f'Pre-Workout: {pre_workout}', 1, 0, 'C', True)
        self.set_fill_color(30, 60, 114)
        self.cell(64, 8, f'Main: {main_workout}', 1, 0, 'C', True)
        self.set_fill_color(23, 162, 184)
        self.cell(63, 8, f'Post-Workout: {post_workout}', 1, 1, 'C', True)
        self.set_text_color(0, 0, 0)
        self.ln(5)
        
    def add_science_note(self, note):
        self.set_fill_color(255, 243, 205)
        self.set_draw_color(255, 193, 7)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(133, 100, 4)
        self.multi_cell(0, 5, f'SCIENCE: {note}', 1, 'L', True)
        self.set_text_color(0, 0, 0)
        self.ln(3)
        
    def add_pre_workout_protocol(self, week_num):
        """User-specified foundation work before main workout - OPTIMIZED FOR AGE 38"""
        self.add_section_title('PRE-WORKOUT FOUNDATION PROTOCOL (30-40 min)', (40, 167, 69))
        self.add_science_note('At age 38, extended sport-specific warm-ups are CRITICAL. Research shows: '
                             '1) Reduces injury risk by 50%+, 2) Improves neural drive and force production, '
                             '3) Increases joint synovial fluid for better mobility. Never skip!')
        
        # Progressive reps based on week - OPTIMIZED for 36 pushups, 15-20 pullups, 36 weighted squats
        pushup_sets = self._get_pushup_progression(week_num)
        pullup_sets = self._get_pullup_progression(week_num)
        squat_sets = self._get_squat_progression(week_num)
        
        widths = [80, 30, 25, 55]
        headers = ['Exercise', 'Sets x Reps', 'Rest', 'Age 38 Progression Notes']
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(40, 167, 69)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        
        pre_exercises = [
            ('1. PUSH-UPS (Full ROM)', pushup_sets, '30-45s', 'Chest to floor, protect shoulders'),
            ('2. PULL-UPS (Mixed Grip OK)', pullup_sets, '60-90s', 'Dead hang, control eccentric'),
            ('3. WEIGHTED SQUATS (Goblet)', squat_sets, '45-60s', 'Below parallel, knee health'),
        ]
        
        for i, (exercise, sets, rest, notes) in enumerate(pre_exercises):
            fill = i % 2 == 0
            self.set_fill_color(232, 245, 233) if fill else self.set_fill_color(255, 255, 255)
            self.cell(widths[0], 8, exercise, 1, 0, 'L', fill)
            self.cell(widths[1], 8, sets, 1, 0, 'C', fill)
            self.cell(widths[2], 8, rest, 1, 0, 'C', fill)
            self.cell(widths[3], 8, notes, 1, 0, 'L', fill)
            self.ln()
        self.ln(3)
        
        # Form cues - UPDATED for age 38 joint protection
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'FORM CUES (AGE 38 JOINT PROTECTION):', 0, 1, 'L')
        self.set_font('Helvetica', '', 8)
        cues = [
            'Push-ups: Hands slightly wider than shoulders, elbows at 45deg (not 90deg flared)',
            'Pull-ups: Full dead hang, controlled descent (3s negative), vary grip weekly',
            'Squats: Sit back into hips FIRST, knees track toes, stop if knee pain'
        ]
        for cue in cues:
            self.cell(5, 5, '*', 0, 0, 'L')
            self.cell(0, 5, cue, 0, 1, 'L')
        self.ln(3)
        
    def _get_pushup_progression(self, week):
        # Target: 36 pushups - conservative progression for age 38
        progressions = {
            1: '3 x 12 = 36',      # Baseline: achieve 36 total
            2: '4 x 10 = 40',      # Volume increase
            3: '3 x 14 = 42',      # Rep increase per set
            4: '4 x 12 = 48'       # Peak week
        }
        return progressions.get(week, '3 x 12 = 36')
        
    def _get_pullup_progression(self, week):
        # Target: 15-20 pullups - realistic for 95kg at age 38
        progressions = {
            1: '3 x 5 = 15',       # Baseline: start conservative
            2: '3 x 6 = 18',       # Add 1 rep per set
            3: '4 x 5 = 20',       # Add a set
            4: '3 x 7 = 21'        # Peak: rep quality over quantity
        }
        return progressions.get(week, '3 x 5 = 15')
        
    def _get_squat_progression(self, week):
        # Target: 36 weighted squats - progressive loading for 180cm/95kg
        progressions = {
            1: '3 x 12 = 36 @ 12kg',   # Start moderate at 95kg BW
            2: '3 x 12 = 36 @ 14kg',   # 2kg increment
            3: '3 x 12 = 36 @ 16kg',   # 2kg increment
            4: '4 x 10 = 40 @ 18kg'    # Volume + load peak
        }
        return progressions.get(week, '3 x 12 = 36 @ 12kg')
        
    def add_main_workout(self, exercises, science_note):
        self.add_section_title('MAIN WORKOUT (60-75 min)', (30, 60, 114))
        self.add_science_note(science_note)
        
        widths = [55, 15, 25, 20, 75]
        headers = ['Exercise', 'Sets', 'Reps/Tempo', 'Rest', 'Technique Notes']
        
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
            self.set_fill_color(240, 248, 255) if fill else self.set_fill_color(255, 255, 255)
            for j, value in enumerate(exercise):
                align = 'L' if j in [0, 4] else 'C'
                self.cell(widths[j], 7, str(value), 1, 0, align, fill)
            self.ln()
        self.ln(3)
        
    def add_post_workout_cardio(self, week_num):
        """2KM walk + 1KM recovery walk - OPTIMIZED for body recomposition at 95kg"""
        self.add_section_title('POST-WORKOUT CARDIO (35-45 min)', (23, 162, 184))
        self.add_science_note('BODY RECOMPOSITION KEY: Post-workout LISS cardio maximizes fat oxidation '
                             'without impairing muscle protein synthesis. At 95kg, walking burns ~85-95 kcal/km. '
                             'This 3km adds ~270 kcal expenditure toward your 500-700 kcal deficit!')
        
        # Progressive walking pace - ADJUSTED for 95kg body weight
        pace_progression = {
            1: ('Moderate', '13-14 min/km', '15-16 min/km'),   # Conservative start
            2: ('Moderate+', '12-13 min/km', '14-15 min/km'),  # Slight increase
            3: ('Brisk', '11-12 min/km', '13-14 min/km'),      # Building
            4: ('Brisk+', '10-11 min/km', '12-13 min/km')      # Peak pace
        }
        
        pace, main_pace, recovery_pace = pace_progression.get(week_num, ('Moderate', '13-14 min/km', '15-16 min/km'))
        
        widths = [70, 40, 40, 40]
        headers = ['Activity', 'Distance', 'Target Pace', 'Calories Burned']
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(23, 162, 184)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        
        cardio = [
            (f'1. Main Walk ({pace})', '2.0 km', main_pace, '~170-190 kcal'),
            ('2. Recovery Walk (Easy)', '1.0 km', recovery_pace, '~85-95 kcal'),
            ('TOTAL', '3.0 km', '35-45 min', '~255-285 kcal'),
        ]
        
        for i, (activity, distance, target_pace, cal) in enumerate(cardio):
            fill = i % 2 == 0
            if i == 2:  # Total row
                self.set_fill_color(23, 162, 184)
                self.set_text_color(255, 255, 255)
                self.set_font('Helvetica', 'B', 8)
            else:
                self.set_fill_color(209, 236, 241) if fill else self.set_fill_color(255, 255, 255)
                self.set_text_color(0, 0, 0)
                self.set_font('Helvetica', '', 8)
            self.cell(widths[0], 7, activity, 1, 0, 'L', True if i == 2 else fill)
            self.cell(widths[1], 7, distance, 1, 0, 'C', True if i == 2 else fill)
            self.cell(widths[2], 7, target_pace, 1, 0, 'C', True if i == 2 else fill)
            self.cell(widths[3], 7, cal, 1, 0, 'C', True if i == 2 else fill)
            self.ln()
        
        self.set_text_color(0, 0, 0)
        self.ln(3)
        
        # Tips - BODY RECOMP FOCUSED
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'BODY RECOMPOSITION WALKING TIPS (95kg -> 80kg):', 0, 1, 'L')
        self.set_font('Helvetica', '', 8)
        tips = [
            'Walking at 95kg burns 30% MORE calories than at 80kg - use this advantage!',
            'Post-workout = peak fat oxidation window (glycogen depleted)',
            'Add inclines or stairs when available for +50% calorie burn',
            'Track steps: aim for 10,000+/day (including this walk)'
        ]
        for tip in tips:
            self.cell(5, 5, '*', 0, 0, 'L')
            self.cell(0, 5, tip, 0, 1, 'L')
        self.ln(2)
        
    def add_stretch_cooldown(self, stretches):
        self.add_section_title('COOL-DOWN STRETCHING (10-15 min)', (100, 50, 100))
        
        widths = [100, 40, 50]
        headers = ['Stretch', 'Duration', 'Done']
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(100, 50, 100)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        for i, (stretch, duration) in enumerate(stretches):
            fill = i % 2 == 0
            self.set_fill_color(245, 240, 250) if fill else self.set_fill_color(255, 255, 255)
            self.cell(widths[0], 6, stretch, 1, 0, 'L', fill)
            self.cell(widths[1], 6, duration, 1, 0, 'C', fill)
            self.cell(widths[2], 6, '[  ]', 1, 0, 'C', fill)
            self.ln()
        self.ln(2)
        
    def add_tracking_section(self):
        self.add_section_title('SESSION TRACKING', (100, 100, 100))
        self.set_font('Helvetica', '', 9)
        
        fields = [
            ('Date:', 50),
            ('Start Time:', 30),
            ('End Time:', 30),
            ('Energy Level (1-10):', 20),
            ('Workout Quality (1-10):', 20),
            ('Sleep Last Night (hrs):', 20),
            ('Pain/Discomfort (location):', 80),
            ('Key Wins Today:', 100),
        ]
        
        for label, line_width in fields:
            self.cell(55, 6, label, 0, 0, 'L')
            self.cell(line_width, 6, '_' * (line_width // 3), 0, 1, 'L')
            
    def add_recovery_day(self, activities, stretches, tips):
        """For rest/mobility days"""
        self.add_section_title('ACTIVE RECOVERY PROTOCOL', (40, 167, 69))
        self.add_science_note('Active recovery with light movement promotes blood flow, reduces DOMS, '
                             'and maintains mobility without impeding muscle repair.')
        
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 6, 'RECOMMENDED ACTIVITIES (choose 1-2):', 0, 1, 'L')
        self.set_font('Helvetica', '', 8)
        for activity in activities:
            self.cell(5, 5, '*', 0, 0, 'L')
            self.cell(0, 5, activity, 0, 1, 'L')
        self.ln(3)
        
        self.add_section_title('MOBILITY ROUTINE', (23, 162, 184))
        widths = [100, 40, 50]
        headers = ['Movement/Stretch', 'Duration', 'Done']
        
        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(23, 162, 184)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 8)
        self.set_text_color(0, 0, 0)
        for i, (stretch, duration) in enumerate(stretches):
            fill = i % 2 == 0
            self.set_fill_color(209, 236, 241) if fill else self.set_fill_color(255, 255, 255)
            self.cell(widths[0], 6, stretch, 1, 0, 'L', fill)
            self.cell(widths[1], 6, duration, 1, 0, 'C', fill)
            self.cell(widths[2], 6, '[  ]', 1, 0, 'C', fill)
            self.ln()
        self.ln(3)
        
        self.add_section_title('RECOVERY TIPS', (100, 100, 100))
        self.set_font('Helvetica', '', 8)
        for tip in tips:
            self.cell(5, 5, '*', 0, 0, 'L')
            self.cell(0, 5, tip, 0, 1, 'L')
        self.ln(2)


# =============================================================================
# WORKOUT CONTENT FOR EACH DAY
# =============================================================================

def get_upper_push_exercises(week):
    """Push-focused upper body: Chest, Shoulders, Triceps
    META-ANALYSIS OPTIMIZED: MWS (5-9 sets) to HWS (10+ sets) per muscle group
    TOTAL WEEKLY CHEST: ~16 sets | SHOULDERS: ~12 sets | TRICEPS: ~10 sets
    """
    base = [
        ('Barbell Bench Press', '4', '6-8 @2-1-2', '3min', 'Heavy compound - protect shoulders at 38'),
        ('Incline Dumbbell Press', '4', '8-10 @2-1-2', '2min', '30deg angle, full stretch, joint-safe'),
        ('Cable Flyes (Low to High)', '3', '12-15 @2-0-2', '60s', 'Constant tension, no joint stress'),
        ('Seated DB Shoulder Press', '4', '8-10 @2-1-2', '2min', 'Neutral grip option for shoulders'),
        ('Lateral Raises', '3', '12-15 @2-0-2', '60s', 'Light weight, control (shoulder health)'),
        ('Rope Tricep Pushdowns', '3', '12-15 @2-0-2', '60s', 'Elbows pinned, full extension'),
        ('Overhead Tricep Extension', '3', '12-15 @2-0-2', '60s', 'Stretch position - elbow care'),
        ('Face Pulls', '3', '15-20 @2-0-2', '45s', 'Rear delt + rotator cuff health'),
    ]
    # Progressive overload: CONSERVATIVE 2.5% increase for age 38
    if week >= 3:
        base[0] = ('Barbell Bench Press', '4', '5-6 @2-1-2', '3min', 'Add 2.5kg from week 2 (age 38 safe)')
        base[1] = ('Incline Dumbbell Press', '4', '6-8 @2-1-2', '2min', 'Add 1-2kg from week 2')
    return base

def get_lower_body_exercises(week):
    """Legs: Quads, Hamstrings, Glutes, Calves
    META-ANALYSIS OPTIMIZED: Target 16-20 sets/muscle for legs
    At 95kg: Focus on controlled movements, knee health priority
    """
    base = [
        ('Barbell Back Squat', '4', '6-8 @3-1-2', '3min', 'Below parallel IF mobility allows'),
        ('Romanian Deadlift', '4', '8-10 @3-1-2', '2min', 'Hip hinge, hamstring stretch, no bounce'),
        ('Walking Lunges', '3', '10 each @2-1-2', '90s', 'Shorter stride at 95kg for knee safety'),
        ('Leg Press', '4', '10-12 @2-1-2', '90s', 'Feet high+wide for glutes, no knee lock'),
        ('Leg Curl (Lying)', '3', '12-15 @2-1-2', '60s', '3s eccentric for hamstring TUT'),
        ('Calf Raises (Seated)', '4', '15-20 @2-2-2', '45s', '2s pause at top, full stretch'),
        ('Hip Thrusts', '4', '12-15 @2-2-2', '90s', 'Glute builder - critical at 38'),
        ('Core: Dead Bug', '3', '10 each @3-0-3', '30s', 'Spine stability for heavy lifts'),
    ]
    if week >= 3:
        base[0] = ('Barbell Back Squat', '4', '5-6 @3-1-2', '3min', 'Add 2.5kg from week 2')
        base[1] = ('Romanian Deadlift', '4', '6-8 @3-1-2', '2min', 'Add 2.5kg from week 2')
    return base

def get_upper_pull_exercises(week):
    """Pull-focused upper body: Back, Biceps, Rear Delts
    META-ANALYSIS OPTIMIZED: High volume back (16+ sets/week)
    At 38: Grip strength and lat engagement focus
    """
    base = [
        ('Barbell Bent Over Row', '4', '6-8 @2-1-2', '2min', '45deg torso, lower chest, squeeze'),
        ('Lat Pulldown (Wide Grip)', '4', '10-12 @2-1-2', '90s', 'Lean back 15deg, chest up'),
        ('Seated Cable Row (V-Bar)', '4', '10-12 @2-1-2', '90s', 'Pull to navel, retract scapula'),
        ('Single Arm DB Row', '3', '10-12 each @2-1-2', '60s', 'Support on bench, full stretch'),
        ('Barbell Curls', '3', '10-12 @2-1-2', '60s', 'No swing, control 3s negative'),
        ('Incline DB Curls', '3', '12-15 @2-1-2', '60s', 'Stretch position, elbow health'),
        ('Reverse Flyes', '3', '15 @2-1-2', '45s', 'Rear delts + posture correction'),
        ('Shrugs (DB or Barbell)', '3', '12-15 @2-2-2', '60s', '2s hold at top, no neck strain'),
    ]
    return base

def get_full_body_exercises(week):
    """Full body compound focus
    BODY RECOMPOSITION DAY: High calorie burn, compound movements
    At 95kg: Maximum metabolic impact
    """
    base = [
        ('Trap Bar Deadlift', '4', '6-8 @3-1-2', '3min', 'Best deadlift variant for 38+ spine'),
        ('Dumbbell Bench Press', '3', '10-12 @2-1-2', '2min', 'Full ROM, stretch at bottom'),
        ('Front Squat (Goblet OK)', '3', '10-12 @2-1-2', '90s', 'Upright torso, quad focus'),
        ('Seated Cable Row', '3', '10-12 @2-1-2', '90s', 'Posture correction day'),
        ('Standing OHP (DB)', '3', '10-12 @2-1-2', '90s', 'Core engaged, no back lean'),
        ('Bulgarian Split Squat', '3', '8 each @2-1-2', '60s', 'Glute/quad unilateral work'),
        ('Farmers Walk', '3', '30 sec', '60s', 'Grip + core + metabolic boost'),
        ('Plank Variations', '3', '45 sec', '30s', 'Front/Side/Front rotation'),
    ]
    return base

def get_upper_stretches():
    return [
        ('Chest Doorway Stretch', '45 sec each side'),
        ('Cross-Body Shoulder Stretch', '30 sec each'),
        ('Overhead Tricep Stretch', '30 sec each'),
        ('Cat-Cow', '10 reps slow'),
        ('Childs Pose', '60 seconds'),
        ('Thread the Needle', '30 sec each'),
    ]

def get_lower_stretches():
    return [
        ('Standing Quad Stretch', '45 sec each'),
        ('Seated Hamstring Stretch', '45 sec each'),
        ('Pigeon Pose', '60 sec each'),
        ('Hip Flexor Stretch', '45 sec each'),
        ('Calf Stretch Against Wall', '30 sec each'),
        ('Figure 4 Stretch', '45 sec each'),
    ]

def get_full_body_stretches():
    return [
        ('Worlds Greatest Stretch', '30 sec each side'),
        ('Downward Dog', '45 seconds'),
        ('Cobra Stretch', '30 seconds'),
        ('Supine Twist', '30 sec each side'),
        ('Happy Baby', '45 seconds'),
        ('Standing Forward Fold', '45 seconds'),
    ]

def get_recovery_stretches():
    return [
        ('Cat-Cow Flow', '2 min slow'),
        ('Thread the Needle', '45 sec each'),
        ('Childs Pose', '90 seconds'),
        ('Supine Spinal Twist', '60 sec each'),
        ('Hip 90/90 Stretch', '45 sec each'),
        ('Foam Roll IT Band', '60 sec each'),
        ('Foam Roll Upper Back', '60 seconds'),
        ('Foam Roll Quads', '60 sec each'),
        ('Deep Breathing', '3 minutes'),
    ]


# =============================================================================
# GENERATE ALL PDFS
# =============================================================================

def create_training_day(week, day, title, focus, exercises_func, stretches):
    pdf = EnhancedWorkoutPDF(week, day, title, focus)
    pdf.add_page()
    pdf.add_duration_box('30-40 min', '60-75 min', '40-50 min')
    
    pdf.add_pre_workout_protocol(week)
    
    # META-ANALYSIS BASED science note (PMC5684266)
    science_note = ('META-ANALYSIS (PMC5684266): Medium-High Weekly Set volume (5-10+ sets/muscle) '
                   'produces 15-23% greater strength gains. Tempo 2-1-2 (slower) protects joints at 38. '
                   'Rest: 2-3min compounds (ATP), 60-90s isolation (metabolic stress). '
                   'BODY RECOMP: Compound lifts preserve muscle in caloric deficit.')
    pdf.add_main_workout(exercises_func(week), science_note)
    
    pdf.add_post_workout_cardio(week)
    pdf.add_stretch_cooldown(stretches)
    
    pdf.add_page()
    pdf.add_tracking_section()
    
    return pdf

def create_recovery_day(week, day, title):
    pdf = EnhancedWorkoutPDF(week, day, title, 'Active Recovery')
    pdf.add_page()
    
    activities = [
        '20-30 min easy walking (Zone 1 cardio) - adds to daily step goal',
        '15-20 min light swimming or aqua jogging - zero impact at 95kg',
        '20 min easy cycling (low resistance) - active recovery for legs',
        '15 min yoga flow (beginner level) - mobility at 38 is critical',
    ]
    
    tips = [
        'SLEEP: 7-9 hours MINIMUM - this is when testosterone peaks for muscle repair',
        'PROTEIN: 1.8-2.2g/kg = 170-210g daily (critical in caloric deficit at 95kg)',
        'HYDRATION: 3.5+ liters water - helps with appetite control too',
        'CALORIC DEFICIT: Stay at 500-700 kcal deficit (2000-2300 kcal intake)',
        'NO ALCOHOL: Impairs protein synthesis by up to 37% - serious impact at 38',
        'NEAT: Non-exercise activity (stairs, standing, fidgeting) burns 200-500 kcal/day',
        'FOAM ROLL: 10-15 min daily reduces DOMS and improves recovery by 20%',
        'SUPPLEMENTS: Creatine 5g/day, Fish oil 2-3g/day, Vitamin D if deficient',
    ]
    
    pdf.add_recovery_day(activities, get_recovery_stretches(), tips)
    
    pdf.add_page()
    pdf.add_tracking_section()
    
    return pdf


def generate_all_pdfs():
    """Generate all 28 daily workout PDFs"""
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'PDFs', 'Daily_Exercises')
    os.makedirs(output_dir, exist_ok=True)
    
    # Weekly schedule structure (4 training days + 3 recovery/rest)
    # Day 1: Upper Push
    # Day 2: Lower Body
    # Day 3: Active Recovery
    # Day 4: Upper Pull
    # Day 5: Full Body
    # Day 6: Active Recovery
    # Day 7: Complete Rest
    
    for week in range(1, 5):
        print(f"\nGenerating Week {week}...")
        
        # Day 1: Upper Body Push
        pdf = create_training_day(week, 1, 'UPPER BODY - PUSH', 'Chest / Shoulders / Triceps',
                                  get_upper_push_exercises, get_upper_stretches())
        filename = f'Week{week}_Day1_Upper_Push.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
        
        # Day 2: Lower Body
        pdf = create_training_day(week, 2, 'LOWER BODY', 'Quads / Hamstrings / Glutes / Calves',
                                  get_lower_body_exercises, get_lower_stretches())
        filename = f'Week{week}_Day2_Lower_Body.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
        
        # Day 3: Active Recovery
        pdf = create_recovery_day(week, 3, 'ACTIVE RECOVERY')
        filename = f'Week{week}_Day3_Recovery.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
        
        # Day 4: Upper Body Pull
        pdf = create_training_day(week, 4, 'UPPER BODY - PULL', 'Back / Biceps / Rear Delts',
                                  get_upper_pull_exercises, get_upper_stretches())
        filename = f'Week{week}_Day4_Upper_Pull.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
        
        # Day 5: Full Body
        pdf = create_training_day(week, 5, 'FULL BODY COMPOUNDS', 'Total Body Strength',
                                  get_full_body_exercises, get_full_body_stretches())
        filename = f'Week{week}_Day5_Full_Body.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
        
        # Day 6: Active Recovery
        pdf = create_recovery_day(week, 6, 'MOBILITY & RECOVERY')
        filename = f'Week{week}_Day6_Mobility.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
        
        # Day 7: Complete Rest
        pdf = create_recovery_day(week, 7, 'COMPLETE REST')
        filename = f'Week{week}_Day7_Rest.pdf'
        pdf.output(os.path.join(output_dir, filename))
        print(f"  Created: {filename}")
    
    print(f"\n{'='*50}")
    print(f"SUCCESS: Generated 28 workout PDFs in:")
    print(f"{output_dir}")
    print(f"{'='*50}")


if __name__ == '__main__':
    generate_all_pdfs()
