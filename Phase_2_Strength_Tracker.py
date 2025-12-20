#!/usr/bin/env python3
"""
PHASE 2: STRENGTH & HYPERTROPHY TRACKER (Weeks 11-20)
💪 Primary Goals: Muscle building, strength gains, aesthetic development 💥
📅 Schedule: 4 workout days, 3 rest days per week

Progressive overload focus with hypertrophy rep ranges and increased training volume.
Building the foundation for both hiking strength and visual muscle development.
"""

import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json

@dataclass
class Exercise:
    name: str
    sets: int
    reps: str
    load_intensity: str
    rest_seconds: int
    form_tips: str
    aesthetic_benefit: str
    completed: bool = False
    actual_weight: Optional[str] = None
    actual_reps: Optional[str] = None
    rpe: Optional[int] = None
    notes: str = ""

@dataclass
class WorkoutDay:
    day: str
    focus: str
    exercises: List[Exercise]
    completed: bool = False
    date_completed: Optional[str] = None
    overall_mood: Optional[str] = None
    energy_level: Optional[int] = None
    duration_minutes: Optional[int] = None

class Phase2Tracker:
    def __init__(self):
        self.week_number = 13  # Starting week for Phase 2
        self.current_date = datetime.date.today()
        self.workout_plan = self._create_workout_plan()
        self.strength_pr_log = {}  # Track personal records
        
    def _create_workout_plan(self) -> Dict[str, WorkoutDay]:
        """Create the complete Phase 2 workout plan - Higher intensity focus"""
        
        # MONDAY - Lower Power
        monday_exercises = [
            Exercise(
                name="Back Squat",
                sets=4, reps="6-8", load_intensity="RPE 7-8, 70-80% 1RM",
                rest_seconds=180,
                form_tips="Knee-friendly depth, tight core, controlled descent",
                aesthetic_benefit="Quad mass development, glute definition"
            ),
            Exercise(
                name="Romanian Deadlift",
                sets=4, reps="8-10", load_intensity="RPE 7-8",
                rest_seconds=120,
                form_tips="Hamstring stretch focus, maintain back arch",
                aesthetic_benefit="Posterior chain definition, hamstring-glute tie-in"
            ),
            Exercise(
                name="Bulgarian Split Squat",
                sets=3, reps="10/leg", load_intensity="RPE 7, DB load",
                rest_seconds=90,
                form_tips="Front foot emphasis, control the descent",
                aesthetic_benefit="Unilateral leg development, glute isolation"
            ),
            Exercise(
                name="Hip Thrust",
                sets=3, reps="12-15", load_intensity="Barbell, RPE 7-8",
                rest_seconds=75,
                form_tips="Glute squeeze at top, neutral spine",
                aesthetic_benefit="Maximum glute activation, rear definition"
            ),
            Exercise(
                name="Calf Raises",
                sets=4, reps="12-15", load_intensity="Heavy load",
                rest_seconds=45,
                form_tips="Slow eccentric, full stretch at bottom",
                aesthetic_benefit="Calf shape and size, lower leg definition"
            )
        ]
        
        # TUESDAY - Upper Power
        tuesday_exercises = [
            Exercise(
                name="Pull-ups/Assisted",
                sets=4, reps="6-10", load_intensity="Bodyweight+",
                rest_seconds=120,
                form_tips="Full ROM, controlled negative, chest to bar",
                aesthetic_benefit="Lat width development, V-taper creation"
            ),
            Exercise(
                name="Incline Barbell Press",
                sets=4, reps="6-8", load_intensity="RPE 8, 70-75%",
                rest_seconds=180,
                form_tips="Upper chest focus, control the negative",
                aesthetic_benefit="Upper chest definition, pec line separation"
            ),
            Exercise(
                name="Bent-over Row",
                sets=4, reps="8-10", load_intensity="RPE 7-8",
                rest_seconds=120,
                form_tips="Neutral spine, pull to lower chest",
                aesthetic_benefit="Back thickness, rear delt development"
            ),
            Exercise(
                name="Overhead Press",
                sets=3, reps="8-10", load_intensity="RPE 7",
                rest_seconds=90,
                form_tips="Core tight, vertical bar path",
                aesthetic_benefit="Shoulder caps, upper body stability"
            ),
            Exercise(
                name="Barbell Curls",
                sets=3, reps="10-12", load_intensity="RPE 7",
                rest_seconds=60,
                form_tips="Strict form, no body swing, squeeze at top",
                aesthetic_benefit="Bicep peak development, arm definition"
            ),
            Exercise(
                name="Close-grip Bench Press",
                sets=3, reps="10-12", load_intensity="RPE 7",
                rest_seconds=60,
                form_tips="Elbows tucked, tricep focus",
                aesthetic_benefit="Tricep mass, arm circumference"
            )
        ]
        
        # WEDNESDAY - HIIT & Core
        wednesday_exercises = [
            Exercise(
                name="Bike Sprint Intervals",
                sets=6, reps="30s sprint/30s easy", load_intensity="RPE 9/RPE 4",
                rest_seconds=0,
                form_tips="All-out effort sprints, complete recovery",
                aesthetic_benefit="Fat burning, leg muscle definition"
            ),
            Exercise(
                name="Plank Variations",
                sets=3, reps="40s each", load_intensity="Front/Side planks",
                rest_seconds=20,
                form_tips="Maintain neutral spine, breathe normally",
                aesthetic_benefit="Core definition, waist tightening"
            ),
            Exercise(
                name="Russian Twists",
                sets=3, reps="20 total", load_intensity="Medicine ball",
                rest_seconds=30,
                form_tips="Controlled rotation, keep feet up",
                aesthetic_benefit="Oblique definition, core strength"
            ),
            Exercise(
                name="Hanging Knee Raises",
                sets=3, reps="8-12", load_intensity="Bodyweight",
                rest_seconds=45,
                form_tips="Control the swing, focus on abs",
                aesthetic_benefit="Lower ab development, V-cut creation"
            )
        ]
        
        # THURSDAY - Unilateral & Prehab
        thursday_exercises = [
            Exercise(
                name="Single-leg RDL",
                sets=3, reps="10/leg", load_intensity="Moderate DB",
                rest_seconds=60,
                form_tips="Balance focus, slow controlled movement",
                aesthetic_benefit="Unilateral posterior chain, stability"
            ),
            Exercise(
                name="Lateral Band Walks",
                sets=3, reps="15/side", load_intensity="Resistance band",
                rest_seconds=30,
                form_tips="Maintain tension, controlled steps",
                aesthetic_benefit="Glute medius, hip width appearance"
            ),
            Exercise(
                name="Single-arm DB Row",
                sets=3, reps="12/arm", load_intensity="RPE 6-7",
                rest_seconds=45,
                form_tips="Support on bench, full ROM",
                aesthetic_benefit="Lat development, back symmetry"
            ),
            Exercise(
                name="Pallof Press",
                sets=3, reps="12/side", load_intensity="Cable resistance",
                rest_seconds=30,
                form_tips="Anti-rotation, maintain posture",
                aesthetic_benefit="Core stability, waist definition"
            )
        ]
        
        # FRIDAY - Full Body Hypertrophy Circuit
        friday_exercises = [
            Exercise(
                name="Goblet Squat",
                sets=3, reps="12-15", load_intensity="Moderate-heavy DB",
                rest_seconds=30,
                form_tips="Full depth, tempo focus",
                aesthetic_benefit="Leg endurance, glute activation"
            ),
            Exercise(
                name="Push-up Variations",
                sets=3, reps="12-15", load_intensity="Diamond/Wide grip",
                rest_seconds=30,
                form_tips="Vary hand position between sets",
                aesthetic_benefit="Chest definition, tricep development"
            ),
            Exercise(
                name="Bent-over DB Row",
                sets=3, reps="12-15", load_intensity="Moderate weight",
                rest_seconds=30,
                form_tips="Squeeze shoulder blades",
                aesthetic_benefit="Back width and thickness"
            ),
            Exercise(
                name="Overhead DB Press",
                sets=3, reps="12-15", load_intensity="Seated/standing",
                rest_seconds=30,
                form_tips="Control the movement, full ROM",
                aesthetic_benefit="Shoulder development, arm definition"
            ),
            Exercise(
                name="Plank to Push-up",
                sets=3, reps="10-12", load_intensity="Bodyweight",
                rest_seconds=30,
                form_tips="Smooth transition, maintain form",
                aesthetic_benefit="Core strength, upper body endurance"
            ),
            Exercise(
                name="Farmer's Walk",
                sets=3, reps="30-45s", load_intensity="Heavy DBs",
                rest_seconds=45,
                form_tips="Upright posture, tight grip",
                aesthetic_benefit="Trap development, forearm size"
            )
        ]
        
        # SATURDAY - Long Walk with Pack
        saturday_exercises = [
            Exercise(
                name="Pack Walk/Hike",
                sets=1, reps="60-90 min", load_intensity="10-15kg pack",
                rest_seconds=0,
                form_tips="Start light, increase 2kg/week gradually",
                aesthetic_benefit="Endurance conditioning, leg definition"
            ),
            Exercise(
                name="Post-Walk Stretch",
                sets=1, reps="15 min", load_intensity="Static stretching",
                rest_seconds=0,
                form_tips="Focus on hips, calves, back",
                aesthetic_benefit="Flexibility, muscle recovery"
            )
        ]
        
        # SUNDAY - Yoga/Mobility + Massage
        sunday_exercises = [
            Exercise(
                name="Yoga Flow",
                sets=1, reps="40-50 min", load_intensity="Vinyasa/Hatha",
                rest_seconds=0,
                form_tips="Focus on tight areas from week's training",
                aesthetic_benefit="Muscle length, flexibility, stress relief"
            ),
            Exercise(
                name="Self-Massage/Foam Roll",
                sets=1, reps="15 min", load_intensity="Full body focus",
                rest_seconds=0,
                form_tips="Include massage ball for trigger points",
                aesthetic_benefit="Muscle quality, recovery enhancement"
            )
        ]
        
        return {
            "Monday": WorkoutDay("Monday", "Lower Power", monday_exercises),
            "Tuesday": WorkoutDay("Tuesday", "Upper Power", tuesday_exercises),
            "Wednesday": WorkoutDay("Wednesday", "REST DAY", []),  # REST DAY
            "Thursday": WorkoutDay("Thursday", "Unilateral & Prehab", thursday_exercises),
            "Friday": WorkoutDay("Friday", "Hypertrophy Circuit", friday_exercises),
            "Saturday": WorkoutDay("Saturday", "REST DAY", []),  # REST DAY
            "Sunday": WorkoutDay("Sunday", "REST DAY", [])  # REST DAY
        }
    
    def display_weekly_plan(self):
        """Display the current week's workout plan"""
        print(f"\n💪 PHASE 2: STRENGTH & HYPERTROPHY - WEEK {self.week_number} 💥")
        print("=" * 80) 
        print(f"📅 Week starting: {self.current_date}")
        print("\n📋 WEEKLY OVERVIEW:")
        print("Focus: Progressive overload, muscle building, aesthetic development")
        
        for day, workout in self.workout_plan.items():
            status = "✅" if workout.completed else "⬜"
            print(f"{status} {day}: {workout.focus}")
        
        print(f"\n😊 Weekly Mood: 😤 💪 😊 😐 😴 | Energy: ⚡⚡⚡⚡⚡ (Rate 1-5)")
        print("🎯 Phase 2 Goals: Increase strength by 15-25%, build visible muscle")
        print("=" * 80)
    
    def log_strength_pr(self, exercise_name: str, weight: str, reps: int):
        """Log a new personal record"""
        pr_key = f"{exercise_name}_{reps}RM"
        self.strength_pr_log[pr_key] = {
            "weight": weight,
            "date": str(datetime.date.today()),
            "week": self.week_number
        }
        print(f"🎉 NEW PR! {exercise_name}: {weight} x {reps} reps")
    
    def display_strength_progress(self):
        """Display strength progression"""
        print("\n💪 STRENGTH PROGRESS LOG")
        print("=" * 40)
        if not self.strength_pr_log:
            print("No PRs logged yet - time to set some records! 🚀")
        else:
            for pr, data in self.strength_pr_log.items():
                exercise = pr.replace("_", " ").title()
                print(f"🏆 {exercise}: {data['weight']} (Week {data['week']})")

# Example usage
if __name__ == "__main__":
    tracker = Phase2Tracker()
    
    print("💪 WELCOME TO PHASE 2: STRENGTH & HYPERTROPHY! 💥")
    print("\nPhase 2 Focus Areas:")
    print("• Progressive overload with heavier weights")
    print("• Hypertrophy rep ranges (6-12 reps)")
    print("• Aesthetic muscle development")
    print("• Strength PR tracking")
    print("• Pack training preparation")
    
    tracker.display_weekly_plan()
    
    print("\n🎯 SAMPLE WORKOUT - TUESDAY (Upper Power)")
    print("="*50)
    # Would show Tuesday's workout details
    
    print("\n📈 NEW FEATURES IN PHASE 2:")
    print("• PR tracking: tracker.log_strength_pr('Back Squat', '100kg', 6)")
    print("• Strength progress: tracker.display_strength_progress()")
    print("• Higher intensity focus (RPE 7-8 range)")
    print("• Pack training preparation for hiking")
    
    print("\n🔥 Ready to build some serious muscle and strength!")
