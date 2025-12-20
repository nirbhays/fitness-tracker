#!/usr/bin/env python3
"""
MASTER FITNESS TRACKER - 11-MONTH TRANSFORMATION PROGRAM
🏔️ Complete system for fat loss, muscle building, and mountain expedition preparation 🎒

Integrates all 4 phases with nutrition tracking, progress monitoring, and comprehensive
logging system. Hindu diet compliant with aesthetic and performance focus.
"""

import datetime
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
import os

# Import phase-specific trackers
try:
    from Phase_1_Foundation_Tracker import Phase1Tracker
    from Phase_2_Strength_Tracker import Phase2Tracker  
    from Phase_3_Endurance_Tracker import Phase3Tracker
    from Phase_4_Peak_Tracker import Phase4Tracker
    from Nutrition_Progress_Tracker import NutritionTracker, Phase
except ImportError:
    print("⚠️ Some tracker modules not found. Ensure all phase trackers are in the same directory.")

class ProgramPhase(Enum):
    PHASE_1 = (1, 10, "Foundation & Fat Loss")
    PHASE_2 = (11, 20, "Strength & Hypertrophy") 
    PHASE_3 = (21, 32, "Endurance & Altitude Prep")
    PHASE_4 = (33, 39, "Peak Hike Simulation")
    
    def __init__(self, start_week: int, end_week: int, description: str):
        self.start_week = start_week
        self.end_week = end_week
        self.description = description

class MasterFitnessTracker:
    def __init__(self, start_date: datetime.date = None):
        self.start_date = start_date or datetime.date.today()
        self.current_week = 1
        self.current_phase = ProgramPhase.PHASE_1
        
        # Initialize all trackers
        self.phase_trackers = {
            ProgramPhase.PHASE_1: Phase1Tracker() if 'Phase1Tracker' in globals() else None,
            ProgramPhase.PHASE_2: Phase2Tracker() if 'Phase2Tracker' in globals() else None,
            ProgramPhase.PHASE_3: Phase3Tracker() if 'Phase3Tracker' in globals() else None,
            ProgramPhase.PHASE_4: Phase4Tracker() if 'Phase4Tracker' in globals() else None
        }
        
        # Initialize nutrition tracker
        self.nutrition_tracker = NutritionTracker(Phase.FOUNDATION) if 'NutritionTracker' in globals() else None
        
        # Progress tracking
        self.program_log = {}
        self.milestone_achievements = []
        self.measurement_log = {}
        
        # Goals and targets
        self.initial_stats = {
            "weight_kg": 93.0,
            "body_fat_percent": None,
            "waist_cm": None,
            "chest_cm": None,
            "arms_cm": None,
            "thighs_cm": None
        }
        
        self.target_stats = {
            "weight_kg": 78.0,
            "body_fat_percent": 12.0,
            "target_hike_date": None
        }
        
        print(f"🎯 Master Fitness Tracker Initialized!")
        print(f"📅 Program Start: {self.start_date}")
        print(f"🗓️ Current Week: {self.current_week}")
        print(f"📊 Current Phase: {self.current_phase.description}")
    
    def update_week(self, week_number: int):
        """Update current week and automatically adjust phase if needed"""
        self.current_week = week_number
        
        # Determine current phase based on week
        for phase in ProgramPhase:
            if phase.start_week <= week_number <= phase.end_week:
                if self.current_phase != phase:
                    self.current_phase = phase
                    self._phase_transition(phase)
                break
        
        print(f"📅 Updated to Week {week_number} - {self.current_phase.description}")
    
    def _phase_transition(self, new_phase: ProgramPhase):
        """Handle transition between phases"""
        print(f"\n🎉 PHASE TRANSITION!")
        print(f"Moving from {self.current_phase.description} to {new_phase.description}")
        
        # Update nutrition tracker phase
        if self.nutrition_tracker:
            phase_map = {
                ProgramPhase.PHASE_1: Phase.FOUNDATION,
                ProgramPhase.PHASE_2: Phase.STRENGTH,
                ProgramPhase.PHASE_3: Phase.ENDURANCE,
                ProgramPhase.PHASE_4: Phase.PEAK
            }
            self.nutrition_tracker.current_phase = phase_map[new_phase]
            self.nutrition_tracker.macro_targets = self.nutrition_tracker._calculate_macro_targets()
        
        # Log transition
        self.program_log[f"Phase_Transition_{new_phase.name}"] = {
            "date": str(datetime.date.today()),
            "week": self.current_week,
            "from_phase": self.current_phase.description,
            "to_phase": new_phase.description
        }
        
        self.current_phase = new_phase
    
    def display_program_overview(self):
        """Display complete 11-month program overview"""
        print(f"\n🏔️ 11-MONTH TRANSFORMATION PROGRAM OVERVIEW 🎒")
        print("=" * 80)
        print(f"📅 Program Duration: 44 weeks ({self.start_date} to estimated completion)")
        print(f"🎯 Primary Goals: Fat loss (15kg), Mountain expedition prep, Aesthetic gains")
        print(f"📊 Current Status: Week {self.current_week} - {self.current_phase.description}")
        
        print(f"\n📋 PHASE BREAKDOWN:")
        for phase in ProgramPhase:
            status = "🔥 CURRENT" if phase == self.current_phase else "✅ COMPLETED" if self.current_week > phase.end_week else "⏳ UPCOMING"
            duration_weeks = phase.end_week - phase.start_week + 1
            print(f"   {status} | Weeks {phase.start_week}-{phase.end_week} ({duration_weeks}w): {phase.description}")
        
        # Progress to expedition
        weeks_remaining = 44 - self.current_week
        months_remaining = weeks_remaining / 4.33
        print(f"\n⏰ Time to Expedition: {weeks_remaining} weeks ({months_remaining:.1f} months)")
        
        if weeks_remaining <= 8:
            print("🚨 FINAL PREPARATION PHASE - Focus on tapering and readiness!")
        elif weeks_remaining <= 16:
            print("🎯 PEAK TRAINING PHASE - Time for maximum effort!")
        else:
            print("💪 BUILD PHASE - Focus on consistent progress!")
    
    def display_current_week_plan(self):
        """Display current week's workout plan"""
        current_tracker = self.phase_trackers.get(self.current_phase)
        
        if current_tracker:
            print(f"\n📋 WEEK {self.current_week} WORKOUT PLAN")
            print("=" * 60)
            current_tracker.display_weekly_plan()
        else:
            print(f"⚠️ Tracker for {self.current_phase.description} not available")
    
    def display_nutrition_plan(self):
        """Display current nutrition plan"""
        if self.nutrition_tracker:
            print(f"\n🥗 NUTRITION PLAN - WEEK {self.current_week}")
            print("=" * 50)
            self.nutrition_tracker.display_daily_targets()
            
            # Show meal plan for current phase
            phase_key = f"Phase {self.current_phase.name[-1]}"
            self.nutrition_tracker.display_meal_plan(phase_key)
        else:
            print("⚠️ Nutrition tracker not available")
    
    def log_body_measurements(self, weight_kg: float, waist_cm: float = None, 
                            chest_cm: float = None, arms_cm: float = None,
                            thighs_cm: float = None, body_fat: float = None):
        """Log body measurements and track progress"""
        today = str(datetime.date.today())
        
        measurements = {
            "date": today,
            "week": self.current_week,
            "phase": self.current_phase.name,
            "weight_kg": weight_kg,
            "waist_cm": waist_cm,
            "chest_cm": chest_cm,
            "arms_cm": arms_cm,
            "thighs_cm": thighs_cm,
            "body_fat_percent": body_fat
        }
        
        self.measurement_log[today] = measurements
        
        # Update nutrition tracker
        if self.nutrition_tracker:
            self.nutrition_tracker.log_daily_metrics(weight_kg=weight_kg, body_fat=body_fat)
        
        # Calculate progress
        weight_loss = self.initial_stats["weight_kg"] - weight_kg
        remaining_loss = weight_kg - self.target_stats["weight_kg"]
        
        print(f"📊 MEASUREMENTS LOGGED - Week {self.current_week}")
        print(f"   ⚖️ Weight: {weight_kg}kg (Lost: {weight_loss:.1f}kg, Remaining: {remaining_loss:.1f}kg)")
        
        if waist_cm:
            print(f"   📏 Waist: {waist_cm}cm")
        if chest_cm:
            print(f"   💪 Chest: {chest_cm}cm")
        if body_fat:
            print(f"   📈 Body Fat: {body_fat}%")
        
        # Check for milestones
        self._check_milestones(weight_loss)
    
    def _check_milestones(self, weight_loss: float):
        """Check and celebrate weight loss milestones"""
        milestones = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0]  # kg milestones
        
        for milestone in milestones:
            if weight_loss >= milestone and milestone not in [m["weight_loss"] for m in self.milestone_achievements]:
                self.milestone_achievements.append({
                    "date": str(datetime.date.today()),
                    "week": self.current_week,
                    "weight_loss": milestone,
                    "phase": self.current_phase.name
                })
                
                print(f"🎉 MILESTONE ACHIEVED! {milestone}kg weight loss!")
                self._milestone_celebration(milestone)
    
    def _milestone_celebration(self, milestone_kg: float):
        """Celebrate milestone achievements"""
        celebrations = {
            2.5: "🎯 Great start! You're building momentum!",
            5.0: "💪 Awesome progress! You're 1/3 of the way there!",
            7.5: "🔥 Halfway to your goal! Keep pushing!",
            10.0: "🚀 Amazing! Only 5kg left to your target!",
            12.5: "🏆 Incredible! You're almost at your goal!",
            15.0: "🎉 GOAL ACHIEVED! You've hit your target weight loss!"
        }
        
        if milestone_kg in celebrations:
            print(f"   {celebrations[milestone_kg]}")
    
    def progress_summary(self, weeks_back: int = 4):
        """Comprehensive progress summary"""
        print(f"\n📈 PROGRESS SUMMARY - LAST {weeks_back} WEEKS")
        print("=" * 60)
        
        # Weight progress
        recent_measurements = [(k, v) for k, v in self.measurement_log.items() 
                             if (datetime.date.today() - datetime.datetime.strptime(k, "%Y-%m-%d").date()).days <= weeks_back * 7]
        
        if recent_measurements:
            recent_measurements.sort(key=lambda x: x[0])
            first_weight = recent_measurements[0][1]["weight_kg"]
            last_weight = recent_measurements[-1][1]["weight_kg"]
            weight_change = last_weight - first_weight
            
            print(f"⚖️ Weight Change: {weight_change:+.1f}kg ({first_weight:.1f} → {last_weight:.1f}kg)")
            
            total_loss = self.initial_stats["weight_kg"] - last_weight
            remaining = last_weight - self.target_stats["weight_kg"]
            progress_percent = (total_loss / 15.0) * 100  # Assuming 15kg total goal
            
            print(f"🎯 Goal Progress: {progress_percent:.1f}% complete ({total_loss:.1f}kg lost, {remaining:.1f}kg remaining)")
        
        # Phase progress
        weeks_in_current_phase = self.current_week - self.current_phase.start_week + 1
        total_weeks_in_phase = self.current_phase.end_week - self.current_phase.start_week + 1
        phase_progress = (weeks_in_current_phase / total_weeks_in_phase) * 100
        
        print(f"📊 Current Phase: {phase_progress:.1f}% complete ({weeks_in_current_phase}/{total_weeks_in_phase} weeks)")
        
        # Overall program progress
        overall_progress = (self.current_week / 44) * 100
        print(f"🗓️ Overall Program: {overall_progress:.1f}% complete ({self.current_week}/44 weeks)")
        
        # Recent milestones
        if self.milestone_achievements:
            recent_milestones = [m for m in self.milestone_achievements 
                               if self.current_week - m["week"] <= weeks_back]
            if recent_milestones:
                print(f"\n🏆 Recent Milestones:")
                for m in recent_milestones:
                    print(f"   • {m['weight_loss']}kg lost (Week {m['week']})")
    
    def expedition_countdown(self, expedition_date: datetime.date = None):
        """Display countdown to mountain expedition"""
        if not expedition_date:
            # Estimate based on 44-week program
            expedition_date = self.start_date + datetime.timedelta(weeks=44)
        
        days_remaining = (expedition_date - datetime.date.today()).days
        weeks_remaining = days_remaining / 7
        
        print(f"\n🏔️ EXPEDITION COUNTDOWN")
        print("=" * 40)
        print(f"📅 Target Date: {expedition_date}")
        print(f"⏰ Days Remaining: {days_remaining}")
        print(f"📊 Weeks Remaining: {weeks_remaining:.1f}")
        
        if days_remaining <= 14:
            print("🚨 FINAL PREPARATION - Taper and rest!")
        elif days_remaining <= 56:
            print("🎯 PEAK SIMULATION - Maximum intensity!")
        elif days_remaining <= 112:
            print("💪 ENDURANCE PHASE - Build that cardio base!")
        else:
            print("🏗️ FOUNDATION PHASE - Build strength and lose fat!")
        
        # Readiness assessment
        if self.current_phase == ProgramPhase.PHASE_4:
            print(f"\n✅ READINESS CHECKLIST:")
            checklist = [
                "6+ hour hiking capability",
                "20kg pack comfort", 
                "Back-to-back day recovery",
                "Zero pain/injury issues",
                "Gear fully tested",
                "Navigation skills practiced",
                "Emergency protocols known"
            ]
            
            for item in checklist:
                print(f"   ⬜ {item}")
    
    def save_all_progress(self, filename: str = None):
        """Save complete program progress to file"""
        if not filename:
            filename = f"master_fitness_progress_week_{self.current_week}.json"
        
        master_data = {
            "program_info": {
                "start_date": str(self.start_date),
                "current_week": self.current_week,
                "current_phase": self.current_phase.name,
                "last_updated": str(datetime.date.today())
            },
            "initial_stats": self.initial_stats,
            "target_stats": self.target_stats,
            "measurement_log": self.measurement_log,
            "milestone_achievements": self.milestone_achievements,
            "program_log": self.program_log
        }
        
        with open(filename, 'w') as f:
            json.dump(master_data, f, indent=2)
        
        print(f"💾 Complete progress saved to {filename}")
    
    def generate_weekly_report(self):
        """Generate comprehensive weekly report"""
        print(f"\n📋 WEEKLY REPORT - WEEK {self.current_week}")
        print("=" * 60)
        print(f"📅 Date: {datetime.date.today()}")
        print(f"🎯 Phase: {self.current_phase.description}")
        
        # Current week focus
        phase_focuses = {
            ProgramPhase.PHASE_1: "Fat loss, movement quality, joint health",
            ProgramPhase.PHASE_2: "Muscle building, strength gains, aesthetic development", 
            ProgramPhase.PHASE_3: "Endurance building, altitude prep, hiking specificity",
            ProgramPhase.PHASE_4: "Peak performance, expedition simulation, tapering"
        }
        
        print(f"🎪 This Week's Focus: {phase_focuses[self.current_phase]}")
        
        # Display current week's plan
        self.display_current_week_plan()
        
        # Show nutrition targets
        if self.nutrition_tracker:
            print(f"\n🥗 NUTRITION TARGETS:")
            targets = self.nutrition_tracker.macro_targets
            print(f"   🔥 Calories: {targets.calories}")
            print(f"   🥩 Protein: {targets.protein_g}g")
            print(f"   🍞 Carbs: {targets.carbs_g}g") 
            print(f"   🥑 Fat: {targets.fat_g}g")
        
        # Progress summary
        self.progress_summary(weeks_back=1)
        
        print(f"\n💪 Week {self.current_week} Action Items:")
        print("• Complete all scheduled workouts")
        print("• Log daily weight and energy levels")
        print("• Follow nutrition plan consistently")
        print("• Get 7-8 hours of sleep nightly")
        print("• Practice stress management techniques")

# Example usage and demonstration
if __name__ == "__main__":
    # Initialize master tracker
    tracker = MasterFitnessTracker()
    
    print("🏔️ WELCOME TO YOUR 11-MONTH TRANSFORMATION! 🎒")
    print("\nThis master tracker coordinates:")
    print("• 4 progressive training phases")
    print("• Hindu diet-compliant nutrition planning")
    print("• Comprehensive progress monitoring")
    print("• Mountain expedition preparation")
    print("• Aesthetic muscle development")
    
    # Display program overview
    tracker.display_program_overview()
    
    # Show current week
    tracker.display_current_week_plan()
    
    # Show countdown
    tracker.expedition_countdown()
    
    print("\n" + "="*70)
    print("📱 MASTER TRACKER USAGE:")
    print("="*70)
    print("• Update week: tracker.update_week(15)")
    print("• Log measurements: tracker.log_body_measurements(90.5, waist_cm=85)")
    print("• Weekly report: tracker.generate_weekly_report()")
    print("• Progress summary: tracker.progress_summary()")
    print("• Save progress: tracker.save_all_progress()")
    
    print("\n🎯 SUCCESS METRICS:")
    print("• Consistent weekly progress on all fronts")
    print("• Zero missed workouts or nutrition days")
    print("• Measurable strength and endurance gains")
    print("• Visible aesthetic improvements")
    print("• Complete expedition readiness")
    
    print("\n🏔️ YOUR MOUNTAIN ADVENTURE AWAITS - LET'S DO THIS! 💪")
