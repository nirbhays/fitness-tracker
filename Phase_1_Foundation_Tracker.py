#!/usr/bin/env python3
"""
PHASE 1: FOUNDATION & FAT LOSS TRACKER (Weeks 1-10)
🏔️ Primary Goals: Fat loss, movement quality, joint health 🏋️‍♂️
📅 Schedule: 4 workout days, 3 rest days per week

This tracker helps you log workouts, track progress, and monitor your journey
towards your mountain hiking and aesthetic goals with optimized recovery.
"""

import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json

@dataclass
class Exercise:
    name: str
    sets: int
    reps: str  # Can be "12-15" or "30s" for time-based
    load_intensity: str
    rest_seconds: int
    form_tips: str
    aesthetic_benefit: str
    completed: bool = False
    actual_weight: Optional[str] = None
    actual_reps: Optional[str] = None
    rpe: Optional[int] = None  # Rate of Perceived Exertion 1-10
    notes: str = ""

@dataclass
class WorkoutDay:
    day: str
    focus: str
    exercises: List[Exercise]
    completed: bool = False
    date_completed: Optional[str] = None
    overall_mood: Optional[str] = None  # 😤 💪 😊 😐 😴
    energy_level: Optional[int] = None  # 1-10
    duration_minutes: Optional[int] = None

class Phase1Tracker:
    def __init__(self):
        self.week_number = 1
        self.current_date = datetime.date.today()
        self.workout_plan = self._create_workout_plan()
        self.progress_log = []
        
    def _create_workout_plan(self) -> Dict[str, WorkoutDay]:
        """Create the complete Phase 1 workout plan"""
        
        # MONDAY - Lower Body Strength
        monday_exercises = [
            Exercise(
                name="Goblet Squat",
                sets=3, reps="12-15", load_intensity="RPE 6-7, 15-25kg DB",
                rest_seconds=60, 
                form_tips="Chest up, knees track toes, full depth",
                aesthetic_benefit="Builds quad definition, shapes glutes"
            ),
            Exercise(
                name="Romanian Deadlift", 
                sets=3, reps="10-12", load_intensity="RPE 6-7, 30-40kg",
                rest_seconds=75,
                form_tips="Hinge at hips, straight back, feel hamstring stretch",
                aesthetic_benefit="Creates hamstring/glute separation, posterior chain"
            ),
            Exercise(
                name="Walking Lunges",
                sets=3, reps="20 steps", load_intensity="Bodyweight",
                rest_seconds=45,
                form_tips="Controlled descent, front knee over ankle",
                aesthetic_benefit="Shapes glutes, improves leg lines"
            ),
            Exercise(
                name="Calf Raises",
                sets=3, reps="15-20", load_intensity="Machine/DB",
                rest_seconds=30,
                form_tips="Full ROM, pause at top, slow eccentric",
                aesthetic_benefit="Defines calf muscles, lower leg shape"
            ),
            Exercise(
                name="Plank",
                sets=3, reps="30-45s", load_intensity="Bodyweight",
                rest_seconds=30,
                form_tips="Neutral spine, tight core, breathe normally",
                aesthetic_benefit="Core stability foundation for V-taper"
            )
        ]
        
        # TUESDAY - Upper Body + Core  
        tuesday_exercises = [
            Exercise(
                name="Lat Pulldown",
                sets=3, reps="10-12", load_intensity="RPE 7, 40-50kg",
                rest_seconds=75,
                form_tips="Wide grip, chest up, pull to upper chest",
                aesthetic_benefit="Creates V-taper back width, lat development"
            ),
            Exercise(
                name="Incline DB Press",
                sets=3, reps="10-12", load_intensity="RPE 6-7, 15-20kg",
                rest_seconds=75,
                form_tips="45° incline, control negative, full stretch",
                aesthetic_benefit="Upper chest definition, pec line separation"
            ),
            Exercise(
                name="Seated Cable Row",
                sets=3, reps="12-15", load_intensity="RPE 6-7",
                rest_seconds=60,
                form_tips="Squeeze shoulder blades, neutral spine",
                aesthetic_benefit="Mid-back thickness, rear delt definition"
            ),
            Exercise(
                name="Lateral Raises",
                sets=3, reps="12-15", load_intensity="RPE 6, 5-8kg",
                rest_seconds=45,
                form_tips="Slight forward lean, thumbs up, control tempo",
                aesthetic_benefit="Shoulder width, capped deltoids"
            ),
            Exercise(
                name="Dead Bug",
                sets=3, reps="10/side", load_intensity="Bodyweight",
                rest_seconds=30,
                form_tips="Slow, controlled, maintain back contact",
                aesthetic_benefit="Deep core stability, flat stomach"
            )
        ]
        
        # WEDNESDAY - Cardio + Mobility
        wednesday_exercises = [
            Exercise(
                name="Incline Walk",
                sets=1, reps="35-40 min", load_intensity="RPE 5-6, 6-8% grade",
                rest_seconds=0,
                form_tips="Joint-friendly cardio, maintain conversation pace",
                aesthetic_benefit="Fat burning, leg endurance, calf definition"
            ),
            Exercise(
                name="Hip Flexor Stretch",
                sets=2, reps="60s/side", load_intensity="Static hold",
                rest_seconds=30,
                form_tips="Couch stretch variation, push hips forward",
                aesthetic_benefit="Hip mobility for better squat depth"
            ),
            Exercise(
                name="Cat-Cow",
                sets=2, reps="10 reps", load_intensity="Controlled",
                rest_seconds=15,
                form_tips="Slow spinal articulation, breath coordination",
                aesthetic_benefit="Posture improvement, spinal health"
            ),
            Exercise(
                name="Foam Roll",
                sets=1, reps="10 min", load_intensity="Self-massage",
                rest_seconds=0,
                form_tips="Focus IT band, glutes, calves - avoid bones",
                aesthetic_benefit="Muscle quality, recovery, definition"
            )
        ]
        
        # THURSDAY - Full Body Circuit
        thursday_exercises = [
            Exercise(
                name="Push-ups",
                sets=3, reps="8-12", load_intensity="Bodyweight/Incline",
                rest_seconds=45,
                form_tips="Full ROM, straight line head to heels",
                aesthetic_benefit="Chest, tricep definition, core stability"
            ),
            Exercise(
                name="Bodyweight Squats",
                sets=3, reps="15-20", load_intensity="Tempo: 3-1-1",
                rest_seconds=45,
                form_tips="Deep squat, pause at bottom, explosive up",
                aesthetic_benefit="Leg endurance, glute activation"
            ),
            Exercise(
                name="Pike Push-ups",
                sets=3, reps="8-10", load_intensity="Bodyweight",
                rest_seconds=45,
                form_tips="Shoulders over hands, press through heels",
                aesthetic_benefit="Shoulder development, upper body strength"
            ),
            Exercise(
                name="Single-leg Glute Bridge",
                sets=3, reps="12/side", load_intensity="Bodyweight",
                rest_seconds=30,
                form_tips="Squeeze glute at top, maintain level hips",
                aesthetic_benefit="Glute isolation, hip stability, rear definition"
            ),
            Exercise(
                name="Mountain Climbers",
                sets=3, reps="20 total", load_intensity="RPE 7-8",
                rest_seconds=45,
                form_tips="Fast but controlled, maintain plank position",
                aesthetic_benefit="Core definition, cardio conditioning"
            )
        ]
        
        # FRIDAY - HIIT + Cardio
        friday_exercises = [
            Exercise(
                name="Incline Walk",
                sets=1, reps="15 min", load_intensity="15% grade, brisk pace",
                rest_seconds=0,
                form_tips="Maintain good posture, swing arms naturally",
                aesthetic_benefit="Fat burning, leg toning, hiking prep"
            ),
            Exercise(
                name="Bike Intervals",
                sets=1, reps="12 min", load_intensity="30s on/30s off, RPE 8-9",
                rest_seconds=0,
                form_tips="All-out effort intervals, easy recovery",
                aesthetic_benefit="Fat burning, leg definition, cardiovascular"
            ),
            Exercise(
                name="Core Circuit",
                sets=3, reps="10 each", load_intensity="Bodyweight",
                rest_seconds=30,
                form_tips="Plank → Side plank → Dead bug → Mountain climbers",
                aesthetic_benefit="Abdominal definition, core strength"
            ),
            Exercise(
                name="Mobility Flow",
                sets=1, reps="10 min", load_intensity="Full body",
                rest_seconds=0,
                form_tips="Hip circles, shoulder rolls, spinal twists",
                aesthetic_benefit="Movement quality, posture, flexibility"
            )
        ]
        
        # SATURDAY - Outdoor Activity
        saturday_exercises = [
            Exercise(
                name="Outdoor Walk/Light Hike",
                sets=1, reps="45-60 min", load_intensity="RPE 4-5",
                rest_seconds=0,
                form_tips="Enjoy nature, moderate pace, proper footwear",
                aesthetic_benefit="Active recovery, mental health, endurance base"
            )
        ]
        
        # SUNDAY - Active Recovery
        sunday_exercises = [
            Exercise(
                name="Yoga/Gentle Stretching",
                sets=1, reps="30-45 min", load_intensity="Light movement",
                rest_seconds=0,
                form_tips="Focus on tight areas, breath awareness",
                aesthetic_benefit="Flexibility, stress relief, muscle quality"
            ),
            Exercise(
                name="Foam Rolling",
                sets=1, reps="15 min", load_intensity="Self-massage",
                rest_seconds=0,
                form_tips="Full body focus, avoid rolling spine directly",
                aesthetic_benefit="Recovery enhancement, muscle definition"
            )
        ]
        
        return {
            "Monday": WorkoutDay("Monday", "Lower Body Strength", monday_exercises),
            "Tuesday": WorkoutDay("Tuesday", "Upper Body + Core", tuesday_exercises), 
            "Wednesday": WorkoutDay("Wednesday", "REST DAY", []),  # REST DAY
            "Thursday": WorkoutDay("Thursday", "Full Body Circuit", thursday_exercises),
            "Friday": WorkoutDay("Friday", "HIIT + Cardio", friday_exercises),
            "Saturday": WorkoutDay("Saturday", "REST DAY", []),  # REST DAY  
            "Sunday": WorkoutDay("Sunday", "REST DAY", [])  # REST DAY
        }
    
    def display_weekly_plan(self):
        """Display the current week's workout plan"""
        print(f"\n🏔️ PHASE 1: FOUNDATION & FAT LOSS - WEEK {self.week_number} 🏋️‍♂️")
        print("=" * 80)
        print(f"📅 Week starting: {self.current_date}")
        print("\n📋 WEEKLY OVERVIEW:")
        
        for day, workout in self.workout_plan.items():
            status = "✅" if workout.completed else "⬜"
            print(f"{status} {day}: {workout.focus}")
        
        print(f"\n😊 Weekly Mood Tracker: 😤 💪 😊 😐 😴 (Circle your dominant mood)")
        print("=" * 80)
    
    def display_daily_workout(self, day: str):
        """Display detailed workout for a specific day"""
        if day not in self.workout_plan:
            print(f"❌ Day '{day}' not found in workout plan")
            return
            
        workout = self.workout_plan[day]
        print(f"\n🎯 {day.upper()} - {workout.focus}")
        print("=" * 60)
        
        for i, exercise in enumerate(workout.exercises, 1):
            status = "✅" if exercise.completed else "⬜"
            print(f"\n{status} {i}. {exercise.name}")
            print(f"   📊 Sets×Reps: {exercise.sets}×{exercise.reps}")
            print(f"   ⚡ Load/Intensity: {exercise.load_intensity}")
            print(f"   ⏱️  Rest: {exercise.rest_seconds}s")
            print(f"   💡 Form: {exercise.form_tips}")
            print(f"   💪 Aesthetic: {exercise.aesthetic_benefit}")
            
            if exercise.completed:
                print(f"   ✏️  Completed: {exercise.actual_weight or 'N/A'} | RPE: {exercise.rpe or 'N/A'}")
                if exercise.notes:
                    print(f"   📝 Notes: {exercise.notes}")
    
    def log_exercise(self, day: str, exercise_index: int, weight: str = None, 
                    reps: str = None, rpe: int = None, notes: str = ""):
        """Log completion of an exercise"""
        if day not in self.workout_plan:
            print(f"❌ Day '{day}' not found")
            return
            
        workout = self.workout_plan[day]
        if exercise_index < 1 or exercise_index > len(workout.exercises):
            print(f"❌ Exercise index {exercise_index} out of range")
            return
            
        exercise = workout.exercises[exercise_index - 1]
        exercise.completed = True
        exercise.actual_weight = weight
        exercise.actual_reps = reps
        exercise.rpe = rpe
        exercise.notes = notes
        
        print(f"✅ Logged: {exercise.name}")
    
    def complete_workout(self, day: str, mood: str = None, energy: int = None, 
                        duration: int = None):
        """Mark entire workout as completed"""
        if day not in self.workout_plan:
            print(f"❌ Day '{day}' not found")
            return
            
        workout = self.workout_plan[day]
        workout.completed = True
        workout.date_completed = str(datetime.date.today())
        workout.overall_mood = mood
        workout.energy_level = energy
        workout.duration_minutes = duration
        
        print(f"🎉 Workout completed: {day} - {workout.focus}")
        
        # Check if all exercises are completed
        incomplete = [ex.name for ex in workout.exercises if not ex.completed]
        if incomplete:
            print(f"⚠️  Note: {len(incomplete)} exercise(s) not logged: {', '.join(incomplete)}")
    
    def weekly_progress_summary(self):
        """Display weekly progress summary"""
        completed_days = sum(1 for workout in self.workout_plan.values() if workout.completed)
        total_exercises = sum(len(workout.exercises) for workout in self.workout_plan.values())
        completed_exercises = sum(sum(1 for ex in workout.exercises if ex.completed) 
                                for workout in self.workout_plan.values())
        
        print(f"\n📊 WEEK {self.week_number} PROGRESS SUMMARY")
        print("=" * 50)
        print(f"✅ Completed Workouts: {completed_days}/7 ({completed_days/7*100:.1f}%)")
        print(f"💪 Completed Exercises: {completed_exercises}/{total_exercises} ({completed_exercises/total_exercises*100:.1f}%)")
        
        # Show mood/energy trends
        moods = [w.overall_mood for w in self.workout_plan.values() if w.overall_mood]
        energies = [w.energy_level for w in self.workout_plan.values() if w.energy_level]
        
        if moods:
            print(f"😊 Week's Moods: {' '.join(moods)}")
        if energies:
            avg_energy = sum(energies) / len(energies)
            print(f"⚡ Average Energy: {avg_energy:.1f}/10")
    
    def save_progress(self, filename: str = None):
        """Save progress to JSON file"""
        if not filename:
            filename = f"phase1_week{self.week_number}_progress.json"
        
        data = {
            "week_number": self.week_number,
            "date": str(self.current_date),
            "workouts": {}
        }
        
        for day, workout in self.workout_plan.items():
            data["workouts"][day] = {
                "focus": workout.focus,
                "completed": workout.completed,
                "date_completed": workout.date_completed,
                "overall_mood": workout.overall_mood,
                "energy_level": workout.energy_level,
                "duration_minutes": workout.duration_minutes,
                "exercises": []
            }
            
            for exercise in workout.exercises:
                data["workouts"][day]["exercises"].append({
                    "name": exercise.name,
                    "completed": exercise.completed,
                    "actual_weight": exercise.actual_weight,
                    "actual_reps": exercise.actual_reps,
                    "rpe": exercise.rpe,
                    "notes": exercise.notes
                })
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Progress saved to {filename}")

# Example usage and interactive session
if __name__ == "__main__":
    # Create tracker instance
    tracker = Phase1Tracker()
    
    print("🏔️ WELCOME TO YOUR PHASE 1 FITNESS TRACKER! 🏋️‍♂️")
    print("\nThis tracker will help you:")
    print("• Log your workouts with detailed exercise tracking")
    print("• Monitor your progress toward fat loss and hiking goals")  
    print("• Track aesthetic improvements (muscle definition)")
    print("• Maintain motivation with mood and energy logging")
    
    # Display current week overview
    tracker.display_weekly_plan()
    
    print("\n" + "="*60)
    print("🎯 SAMPLE DAILY WORKOUT - MONDAY")
    print("="*60)
    tracker.display_daily_workout("Monday")
    
    print("\n" + "="*60)
    print("📝 HOW TO USE THIS TRACKER:")
    print("="*60)
    print("1. View daily workout: tracker.display_daily_workout('Monday')")
    print("2. Log exercise: tracker.log_exercise('Monday', 1, weight='20kg', rpe=7)")
    print("3. Complete workout: tracker.complete_workout('Monday', mood='💪', energy=8)")
    print("4. Weekly summary: tracker.weekly_progress_summary()")
    print("5. Save progress: tracker.save_progress()")
    
    print("\n🎉 Ready to start your transformation journey!")
    print("Focus: Fat Loss + Mountain Prep + Aesthetic Gains")
    print("Remember: Consistency beats perfection! 💪")
