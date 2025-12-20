#!/usr/bin/env python3
"""
PHASE 3: ENDURANCE & ALTITUDE PREP TRACKER (Weeks 21-32)
🚶‍♂️ Primary Goals: Aerobic capacity, hiking-specific strength, altitude preparation ⛰️
📅 Schedule: 4 workout days, 3 rest days per week

Focus shifts to endurance training, hiking simulation, and mountain-specific conditioning
while maintaining strength and aesthetic gains from previous phases.
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
    elevation_gain: Optional[str] = None  # For hiking activities
    pack_weight: Optional[str] = None

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
    weather_conditions: Optional[str] = None  # For outdoor activities

class Phase3Tracker:
    def __init__(self):
        self.week_number = 25  # Starting week for Phase 3
        self.current_date = datetime.date.today()
        self.workout_plan = self._create_workout_plan()
        self.hiking_log = {}  # Track hiking progress
        self.altitude_prep_log = []
        
    def _create_workout_plan(self) -> Dict[str, WorkoutDay]:
        """Create the complete Phase 3 workout plan - Endurance and altitude focus"""
        
        # MONDAY - Hiking Simulation
        monday_exercises = [
            Exercise(
                name="Incline Treadmill Hike",
                sets=1, reps="45-60 min", load_intensity="RPE 6-7, 8-12% grade",
                rest_seconds=0,
                form_tips="Build gradually, maintain conversation pace",
                aesthetic_benefit="Leg endurance, calf definition, fat burning"
            ),
            Exercise(
                name="Weighted Step-ups",
                sets=3, reps="15/leg", load_intensity="10-15kg pack/DBs",
                rest_seconds=60,
                form_tips="High box, full hip extension, controlled descent",
                aesthetic_benefit="Glute/quad functional strength, hiking-specific power"
            ),
            Exercise(
                name="Single-leg Calf Raises",
                sets=3, reps="12/leg", load_intensity="Bodyweight + pack",
                rest_seconds=45,
                form_tips="Full ROM, balance focus, slow negative",
                aesthetic_benefit="Calf endurance, ankle stability for rocky terrain"
            ),
            Exercise(
                name="Core Stability Circuit",
                sets=2, reps="45s each", load_intensity="Plank variations with pack",
                rest_seconds=30,
                form_tips="Maintain form under load",
                aesthetic_benefit="Functional core strength, pack carrying stability"
            )
        ]
        
        # TUESDAY - Strength Maintenance  
        tuesday_exercises = [
            Exercise(
                name="Trap Bar Deadlift",
                sets=3, reps="6-8", load_intensity="RPE 7-8",
                rest_seconds=120,
                form_tips="Spine-friendly variation, drive through heels",
                aesthetic_benefit="Full posterior chain, back thickness"
            ),
            Exercise(
                name="Incline DB Press",
                sets=3, reps="8-10", load_intensity="RPE 7",
                rest_seconds=90,
                form_tips="Maintain muscle mass focus",
                aesthetic_benefit="Upper chest maintenance, shoulder stability"
            ),
            Exercise(
                name="Cable Row",
                sets=3, reps="10-12", load_intensity="RPE 7",
                rest_seconds=75,
                form_tips="Mid-back focus, scapular retraction",
                aesthetic_benefit="V-taper maintenance, postural strength"
            ),
            Exercise(
                name="Lateral Raises",
                sets=3, reps="12-15", load_intensity="RPE 6-7",
                rest_seconds=45,
                form_tips="Time under tension, control tempo",
                aesthetic_benefit="Shoulder width maintenance, deltoid definition"
            ),
            Exercise(
                name="Face Pulls",
                sets=3, reps="15-20", load_intensity="Light-moderate",
                rest_seconds=30,
                form_tips="Rear delt focus, external rotation",
                aesthetic_benefit="Rear delt definition, shoulder health"
            )
        ]
        
        # WEDNESDAY - Incline Intervals
        wednesday_exercises = [
            Exercise(
                name="Treadmill Hill Intervals",
                sets=8, reps="3 min work/2 min recovery", load_intensity="RPE 7-8/RPE 4-5",
                rest_seconds=0,
                form_tips="Steep incline (10-15%), maintain form under fatigue",
                aesthetic_benefit="VO2 max improvement, leg muscle endurance"
            ),
            Exercise(
                name="Breathing Exercises",
                sets=3, reps="2 min each", load_intensity="Box breathing, altitude prep",
                rest_seconds=60,
                form_tips="4-4-4-4 count, focus on efficiency",
                aesthetic_benefit="Respiratory muscle training, altitude adaptation"
            ),
            Exercise(
                name="Ankle Mobility",
                sets=2, reps="10/direction", load_intensity="Bodyweight",
                rest_seconds=15,
                form_tips="Full ROM, both directions",
                aesthetic_benefit="Ankle flexibility for uneven terrain"
            )
        ]
        
        # THURSDAY - Active Recovery + Core
        thursday_exercises = [
            Exercise(
                name="Easy Bike/Swim",
                sets=1, reps="30 min", load_intensity="RPE 4-5",
                rest_seconds=0,
                form_tips="Low impact, recovery focus",
                aesthetic_benefit="Active recovery, cardiovascular maintenance"
            ),
            Exercise(
                name="Core Stability Sequence",
                sets=1, reps="20 min", load_intensity="Varied exercises",
                rest_seconds=30,
                form_tips="Bird-dog, side plank, dead bug progressions",
                aesthetic_benefit="Deep core stability, postural endurance"
            ),
            Exercise(
                name="Hip Flexor Release",
                sets=2, reps="90s/side", load_intensity="Static stretch",
                rest_seconds=30,
                form_tips="Couch stretch, focus on tight hip flexors",
                aesthetic_benefit="Hip mobility for long hiking days"
            )
        ]
        
        # FRIDAY - Strength + Plyometrics
        friday_exercises = [
            Exercise(
                name="Goblet Squat",
                sets=3, reps="8-10", load_intensity="Moderate load, explosive up",
                rest_seconds=75,
                form_tips="Slow down, explosive up, power focus",
                aesthetic_benefit="Leg power, glute activation"
            ),
            Exercise(
                name="Box Step-ups (Explosive)",
                sets=3, reps="8/leg", load_intensity="Bodyweight, focus on speed",
                rest_seconds=60,
                form_tips="Drive through heel, fast up, controlled down",
                aesthetic_benefit="Hiking-specific power, unilateral strength"
            ),
            Exercise(
                name="Kettlebell Swings",
                sets=3, reps="15-20", load_intensity="Moderate KB",
                rest_seconds=60,
                form_tips="Hip hinge pattern, explosive hip extension",
                aesthetic_benefit="Posterior chain power, cardio conditioning"
            ),
            Exercise(
                name="Medicine Ball Slams",
                sets=3, reps="12", load_intensity="Heavy ball",
                rest_seconds=45,
                form_tips="Full body engagement, controlled slam",
                aesthetic_benefit="Core power, upper body conditioning"
            ),
            Exercise(
                name="Jump Squats",
                sets=3, reps="8-10", load_intensity="Bodyweight",
                rest_seconds=60,
                form_tips="Soft landing, full extension",
                aesthetic_benefit="Leg power, plyometric conditioning"
            )
        ]
        
        # SATURDAY - Long Hike (Pack Training)
        saturday_exercises = [
            Exercise(
                name="Long Hike/Trail Walk",
                sets=1, reps="3-4 hours", load_intensity="15-20kg pack, varied terrain",
                rest_seconds=0,
                form_tips="Steeper terrain, practice nutrition/hydration",
                aesthetic_benefit="Ultimate endurance conditioning, mental toughness"
            ),
            Exercise(
                name="Post-Hike Recovery",
                sets=1, reps="20 min", load_intensity="Stretching + hydration",
                rest_seconds=0,
                form_tips="Focus on tight areas, electrolyte replacement",
                aesthetic_benefit="Recovery enhancement, flexibility maintenance"
            )
        ]
        
        # SUNDAY - Rest/Mobility
        sunday_exercises = [
            Exercise(
                name="Restorative Yoga",
                sets=1, reps="45-60 min", load_intensity="Gentle flow",
                rest_seconds=0,
                form_tips="Focus on tight areas from week's training",
                aesthetic_benefit="Flexibility, stress relief, muscle recovery"
            ),
            Exercise(
                name="Foam Rolling + Massage",
                sets=1, reps="20 min", load_intensity="Full body focus",
                rest_seconds=0,
                form_tips="Include massage ball, focus on IT bands",
                aesthetic_benefit="Muscle quality, preparation for next week"
            ),
            Exercise(
                name="Contrast Bath/Shower",
                sets=3, reps="3 min hot/1 min cold", load_intensity="Temperature therapy",
                rest_seconds=0,
                form_tips="End on cold, focus on legs",
                aesthetic_benefit="Recovery enhancement, circulation"
            )
        ]
        
        return {
            "Monday": WorkoutDay("Monday", "Hiking Simulation", monday_exercises),
            "Tuesday": WorkoutDay("Tuesday", "Strength Maintenance", tuesday_exercises),
            "Wednesday": WorkoutDay("Wednesday", "REST DAY", []),  # REST DAY
            "Thursday": WorkoutDay("Thursday", "Strength + Plyometrics", friday_exercises),  # Moved Friday here
            "Friday": WorkoutDay("Friday", "Long Hike Training", saturday_exercises),  # Moved Saturday here
            "Saturday": WorkoutDay("Saturday", "REST DAY", []),  # REST DAY
            "Sunday": WorkoutDay("Sunday", "REST DAY", [])  # REST DAY
        }
    
    def display_weekly_plan(self):
        """Display the current week's workout plan"""
        print(f"\n🚶‍♂️ PHASE 3: ENDURANCE & ALTITUDE PREP - WEEK {self.week_number} ⛰️")
        print("=" * 80)
        print(f"📅 Week starting: {self.current_date}")
        print("\n📋 WEEKLY OVERVIEW:")
        print("Focus: Hiking endurance, altitude preparation, maintaining strength gains")
        
        for day, workout in self.workout_plan.items():
            status = "✅" if workout.completed else "⬜"
            print(f"{status} {day}: {workout.focus}")
        
        print(f"\n🎯 Phase 3 Targets:")
        print("• 3-4 hour hikes with 15-20kg pack")
        print("• Improved VO2 max and respiratory efficiency") 
        print("• Maintain strength gains from Phase 2")
        print("• Altitude adaptation protocols")
        print("=" * 80)
    
    def log_hiking_session(self, distance_km: float, elevation_gain_m: int, 
                          pack_weight_kg: int, duration_min: int, conditions: str):
        """Log hiking session details"""
        hike_data = {
            "date": str(datetime.date.today()),
            "week": self.week_number,
            "distance_km": distance_km,
            "elevation_gain_m": elevation_gain_m,
            "pack_weight_kg": pack_weight_kg,
            "duration_min": duration_min,
            "conditions": conditions,
            "pace_min_per_km": duration_min / distance_km if distance_km > 0 else 0
        }
        
        hike_key = f"Week_{self.week_number}_Hike"
        self.hiking_log[hike_key] = hike_data
        
        print(f"🥾 Hiking session logged:")
        print(f"   Distance: {distance_km}km | Elevation: {elevation_gain_m}m")
        print(f"   Pack: {pack_weight_kg}kg | Duration: {duration_min}min")
        print(f"   Pace: {hike_data['pace_min_per_km']:.1f} min/km")
    
    def display_hiking_progress(self):
        """Display hiking progression over weeks"""
        print("\n🥾 HIKING PROGRESS LOG")
        print("=" * 60)
        if not self.hiking_log:
            print("No hikes logged yet - time to hit the trails! 🌲")
        else:
            for hike_key, data in self.hiking_log.items():
                print(f"📈 {hike_key}:")
                print(f"    {data['distance_km']}km | +{data['elevation_gain_m']}m | {data['pack_weight_kg']}kg")
                print(f"    Pace: {data['pace_min_per_km']:.1f} min/km | Conditions: {data['conditions']}")
    
    def altitude_prep_notes(self):
        """Display altitude preparation tips and tracking"""
        print("\n🏔️ ALTITUDE PREPARATION CHECKLIST")
        print("=" * 50)
        print("📋 Key Preparation Elements:")
        print("• Breathing exercises (daily 10+ minutes)")
        print("• Gradual pack weight increases")
        print("• Incline training (8-15% grades)")
        print("• Hydration protocol practice")
        print("• Sleep quality optimization")
        print("• Iron levels monitoring (for oxygen transport)")
        
        print("\n💡 Altitude Adaptation Tips:")
        print("• Practice nose breathing during cardio")
        print("• Box breathing: 4-4-4-4 count")
        print("• Hypoxic training if available")
        print("• Simulate hiking conditions (pack, terrain)")

# Example usage
if __name__ == "__main__":
    tracker = Phase3Tracker()
    
    print("🚶‍♂️ WELCOME TO PHASE 3: ENDURANCE & ALTITUDE PREP! ⛰️")
    print("\nPhase 3 Key Features:")
    print("• Hiking-specific conditioning")
    print("• Altitude preparation protocols")
    print("• Endurance capacity building")
    print("• Pack weight progression")
    print("• Strength maintenance focus")
    
    tracker.display_weekly_plan()
    tracker.altitude_prep_notes()
    
    print("\n📊 NEW TRACKING FEATURES:")
    print("• Hiking log: tracker.log_hiking_session(8.5, 800, 18, 180, 'Sunny')")
    print("• Progress view: tracker.display_hiking_progress()")
    print("• Altitude prep: tracker.altitude_prep_notes()")
    
    print("\n🎯 Phase 3 Success Metrics:")
    print("• Complete 4+ hour hikes with 20kg pack")
    print("• Maintain sub-8 min/km pace on moderate terrain")
    print("• Improved breathing efficiency at exertion")
    print("• Zero hiking-related injuries or pain")
    
    print("\n⛰️ Get ready to conquer those mountains!")
