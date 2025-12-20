#!/usr/bin/env python3
"""
COMPREHENSIVE NUTRITION & PROGRESS TRACKER
🥗 Hindu Diet-Compliant Meal Planning & Macro Tracking 📊

Supports all 4 phases with automatic calorie/macro adjustments,
meal planning, supplement tracking, and progress monitoring.
"""

import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import json
from enum import Enum

class Phase(Enum):
    FOUNDATION = "Phase 1: Foundation & Fat Loss"
    STRENGTH = "Phase 2: Strength & Hypertrophy" 
    ENDURANCE = "Phase 3: Endurance & Altitude Prep"
    PEAK = "Phase 4: Peak Hike Simulation"

@dataclass
class MacroTargets:
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int
    phase: Phase

@dataclass
class Meal:
    name: str
    time: str
    calories: int
    protein_g: float
    carbs_g: float
    fat_g: float
    foods: List[str]
    hindu_compliant: bool = True

@dataclass
class Supplement:
    name: str
    dosage: str
    timing: str
    purpose: str
    taken: bool = False

@dataclass
class DailyLog:
    date: str
    weight_kg: Optional[float] = None
    body_fat_percent: Optional[float] = None
    energy_level: Optional[int] = None  # 1-10
    sleep_hours: Optional[float] = None
    sleep_quality: Optional[int] = None  # 1-10
    stress_level: Optional[int] = None  # 1-10
    workout_completed: bool = False
    meals_logged: List[Meal] = field(default_factory=list)
    supplements_taken: List[Supplement] = field(default_factory=list)
    notes: str = ""

class NutritionTracker:
    def __init__(self, current_phase: Phase = Phase.FOUNDATION):
        self.current_phase = current_phase
        self.current_weight = 93.0  # Starting weight
        self.target_weight = 78.0   # Goal weight
        self.height_cm = 182
        self.age = 38
        self.activity_multiplier = 1.6  # Moderately active
        
        self.macro_targets = self._calculate_macro_targets()
        self.meal_templates = self._create_meal_templates()
        self.supplement_protocol = self._create_supplement_protocol()
        self.daily_logs = {}
        
    def _calculate_macro_targets(self) -> MacroTargets:
        """Calculate macro targets based on current phase"""
        # Base metabolic rate (Mifflin-St Jeor for men)
        bmr = (10 * self.current_weight) + (6.25 * self.height_cm) - (5 * self.age) + 5
        tdee = bmr * self.activity_multiplier
        
        if self.current_phase == Phase.FOUNDATION:
            # 25% deficit for fat loss
            calories = int(tdee * 0.75)
            protein_g = int((calories * 0.35) / 4)  # 35% protein
            carbs_g = int((calories * 0.30) / 4)    # 30% carbs  
            fat_g = int((calories * 0.35) / 9)      # 35% fat
            
        elif self.current_phase == Phase.STRENGTH:
            # Slight deficit for body recomposition
            calories = int(tdee * 0.85)
            protein_g = int((calories * 0.30) / 4)  # 30% protein
            carbs_g = int((calories * 0.40) / 4)    # 40% carbs
            fat_g = int((calories * 0.30) / 9)      # 30% fat
            
        elif self.current_phase == Phase.ENDURANCE:
            # Increased carbs for training demands
            calories = int(tdee * 0.95)
            protein_g = int((calories * 0.25) / 4)  # 25% protein
            carbs_g = int((calories * 0.45) / 4)    # 45% carbs
            fat_g = int((calories * 0.30) / 9)      # 30% fat
            
        else:  # PEAK phase
            # Full maintenance for performance
            calories = int(tdee)
            protein_g = int((calories * 0.25) / 4)  # 25% protein
            carbs_g = int((calories * 0.50) / 4)    # 50% carbs
            fat_g = int((calories * 0.25) / 9)      # 25% fat
        
        return MacroTargets(calories, protein_g, carbs_g, fat_g, self.current_phase)
    
    def _create_meal_templates(self) -> Dict[str, List[Meal]]:
        """Create Hindu diet-compliant meal templates for each phase"""
        
        # Phase 1: Fat Loss Meals (2,100-2,200 kcal)
        phase1_meals = [
            Meal("Pre-Workout", "6:00 AM", 50, 2, 8, 0, 
                 ["Black coffee", "5g BCAA"]),
            Meal("Breakfast", "8:00 AM", 400, 28, 30, 18,
                 ["2-egg omelette", "2 slices ezekiel bread", "1 tsp ghee", "Green tea"]),
            Meal("Mid-Morning", "10:30 AM", 200, 6, 15, 12,
                 ["1 medium apple", "15g almonds"]),
            Meal("Lunch", "1:00 PM", 500, 45, 15, 28,
                 ["150g grilled chicken", "Large mixed salad", "2 boiled eggs", "Olive oil dressing"]),
            Meal("Pre-Workout", "4:00 PM", 150, 2, 35, 0,
                 ["1 medium banana", "Black coffee"]),
            Meal("Post-Workout", "7:00 PM", 160, 40, 4, 2,
                 ["40g whey protein shake"]),
            Meal("Dinner", "8:00 PM", 600, 35, 60, 18,
                 ["100g basmati rice", "150g fish curry", "Mixed vegetables", "1 tsp coconut oil"]),
            Meal("Evening", "9:30 PM", 0, 0, 0, 0,
                 ["Green tea"])
        ]
        
        # Phase 2: Muscle Building Meals (2,400-2,500 kcal)
        phase2_meals = [
            Meal("Pre-Workout", "6:00 AM", 50, 2, 8, 0,
                 ["Black coffee", "5g BCAA"]),
            Meal("Breakfast", "8:00 AM", 500, 32, 45, 18,
                 ["2-egg omelette", "2 slices ezekiel bread", "1 medium sweet potato", "1 tsp ghee"]),
            Meal("Mid-Morning", "10:30 AM", 250, 8, 20, 12,
                 ["1 medium banana", "15g almonds", "5g honey"]),
            Meal("Lunch", "1:00 PM", 600, 48, 35, 28,
                 ["150g grilled chicken", "100g brown rice", "Large salad", "2 boiled eggs"]),
            Meal("Pre-Workout", "4:00 PM", 200, 5, 40, 2,
                 ["1 medium banana", "10g dates", "Black coffee"]),
            Meal("Post-Workout", "7:00 PM", 200, 50, 8, 2,
                 ["50g whey protein", "1 cup milk"]),
            Meal("Dinner", "8:00 PM", 700, 40, 80, 20,
                 ["150g basmati rice", "150g chicken curry", "Dal", "Vegetables", "Ghee"]),
            Meal("Evening", "10:00 PM", 100, 8, 12, 0,
                 ["1 cup warm milk", "Turmeric"])
        ]
        
        # Phase 3: Endurance Meals (2,600-2,800 kcal)
        phase3_meals = [
            Meal("Pre-Workout", "5:30 AM", 150, 5, 35, 0,
                 ["1 banana", "10g dates", "Black coffee", "BCAA"]),
            Meal("Breakfast", "8:00 AM", 550, 28, 65, 18,
                 ["3-egg omelette", "2 slices bread", "1 large sweet potato", "Ghee"]),
            Meal("Mid-Morning", "10:30 AM", 300, 10, 45, 8,
                 ["1 apple", "20g mixed nuts", "10g honey"]),
            Meal("Lunch", "1:00 PM", 650, 45, 55, 25,
                 ["150g chicken", "150g brown rice", "Large salad", "2 eggs", "Avocado"]),
            Meal("Pre-Long Hike", "4:00 PM", 250, 8, 50, 5,
                 ["Energy balls", "Banana", "Coffee"]),
            Meal("Post-Workout", "7:30 PM", 220, 50, 10, 3,
                 ["50g whey protein", "Milk", "5g honey"]),
            Meal("Dinner", "8:30 PM", 800, 45, 100, 25,
                 ["200g basmati rice", "150g fish curry", "Dal", "Vegetables", "Ghee"]),
            Meal("Evening", "10:00 PM", 100, 8, 12, 0,
                 ["Warm milk", "Turmeric", "Cardamom"])
        ]
        
        # Phase 4: Peak Performance Meals (2,800-3,000 kcal)
        phase4_meals = [
            Meal("Early Pre-Hike", "5:00 AM", 300, 12, 55, 8,
                 ["Oatmeal", "Banana", "Nuts", "Honey", "Coffee"]),
            Meal("Breakfast", "8:00 AM", 600, 32, 75, 20,
                 ["3-egg omelette", "3 slices bread", "Sweet potato", "Ghee", "Fruit"]),
            Meal("Mid-Morning", "11:00 AM", 350, 12, 50, 10,
                 ["Trail mix", "Dried fruits", "Nuts"]),
            Meal("Lunch", "1:00 PM", 700, 50, 65, 28,
                 ["200g chicken", "150g rice", "Large salad", "2 eggs", "Avocado"]),
            Meal("Pre-Long Hike", "3:30 PM", 300, 10, 60, 8,
                 ["Energy bars", "Banana", "Electrolyte drink"]),
            Meal("During Hike", "Throughout", 200, 5, 50, 0,
                 ["Sports drink", "Energy gels", "Dried fruits"]),
            Meal("Post-Hike", "7:00 PM", 250, 50, 15, 3,
                 ["50g whey protein", "Milk", "Recovery drink"]),
            Meal("Dinner", "8:30 PM", 900, 50, 120, 28,
                 ["200g rice", "200g chicken curry", "Dal", "Vegetables", "Ghee"]),
            Meal("Evening", "10:30 PM", 150, 12, 18, 2,
                 ["Warm milk", "Honey", "Almonds"])
        ]
        
        return {
            "Phase 1": phase1_meals,
            "Phase 2": phase2_meals, 
            "Phase 3": phase3_meals,
            "Phase 4": phase4_meals
        }
    
    def _create_supplement_protocol(self) -> List[Supplement]:
        """Create comprehensive supplement protocol"""
        return [
            Supplement("Whey Protein", "25-50g", "Post-workout", 
                      "Muscle recovery and growth"),
            Supplement("BCAA", "10g", "Intra-workout", 
                      "Muscle preservation during training"),
            Supplement("Multivitamin", "2 tablets", "Morning & Evening",
                      "General micronutrient support"),
            Supplement("Vitamin D3", "2,000-4,000 IU", "Morning with fat",
                      "Bone health, immune system, hormone support"),
            Supplement("Iron + Vitamin C", "18mg Fe + 100mg C", "Morning empty stomach",
                      "Address mild anemia, oxygen transport"),
            Supplement("Ashwagandha", "300mg", "Evening",
                      "TSH/testosterone support, stress management"),
            Supplement("Omega-3", "2g EPA/DHA", "With meals",
                      "Anti-inflammatory, recovery, brain health"),
            Supplement("Magnesium", "400mg", "Before bed",
                      "Sleep quality, muscle recovery, relaxation"),
            Supplement("Creatine", "5g", "Post-workout",
                      "Strength, power, muscle volume"),
            Supplement("Electrolytes", "As needed", "During long hikes",
                      "Hydration, cramping prevention")
        ]
    
    def display_daily_targets(self):
        """Display current phase nutrition targets"""
        targets = self.macro_targets
        print(f"\n🎯 {targets.phase.value.upper()} - DAILY TARGETS")
        print("=" * 60)
        print(f"📊 Calories: {targets.calories} kcal")
        print(f"🥩 Protein: {targets.protein_g}g ({targets.protein_g*4}/{targets.calories*100:.0f}%)")
        print(f"🍞 Carbs: {targets.carbs_g}g ({targets.carbs_g*4}/{targets.calories*100:.0f}%)")
        print(f"🥑 Fat: {targets.fat_g}g ({targets.fat_g*9}/{targets.calories*100:.0f}%)")
        
        # Calculate per kg protein
        protein_per_kg = targets.protein_g / self.current_weight
        print(f"💪 Protein per kg: {protein_per_kg:.1f}g/kg (Target: 2.0g/kg)")
        
        if protein_per_kg < 1.8:
            print("⚠️  Consider increasing protein intake")
        elif protein_per_kg > 2.2:
            print("✅ Excellent protein intake for muscle building")
    
    def display_meal_plan(self, phase_key: str = None):
        """Display meal plan for current or specified phase"""
        if not phase_key:
            phase_key = f"Phase {self.current_phase.name[0]}"
        
        meals = self.meal_templates.get(phase_key, [])
        total_cals = sum(m.calories for m in meals)
        total_protein = sum(m.protein_g for m in meals)
        total_carbs = sum(m.carbs_g for m in meals)
        total_fat = sum(m.fat_g for m in meals)
        
        print(f"\n🍽️ DAILY MEAL PLAN - {phase_key.upper()}")
        print("=" * 70)
        
        for meal in meals:
            print(f"\n⏰ {meal.time} - {meal.name}")
            print(f"   🔥 {meal.calories} kcal | P: {meal.protein_g}g | C: {meal.carbs_g}g | F: {meal.fat_g}g")
            print(f"   🥗 Foods: {', '.join(meal.foods)}")
        
        print(f"\n📊 DAILY TOTALS:")
        print(f"   🔥 Calories: {total_cals} kcal")
        print(f"   🥩 Protein: {total_protein}g ({total_protein/self.current_weight:.1f}g/kg)")
        print(f"   🍞 Carbs: {total_carbs}g")
        print(f"   🥑 Fat: {total_fat}g")
    
    def display_supplement_protocol(self):
        """Display supplement recommendations"""
        print(f"\n💊 SUPPLEMENT PROTOCOL - ALL PHASES")
        print("=" * 60)
        
        morning_supps = [s for s in self.supplement_protocol if "morning" in s.timing.lower()]
        workout_supps = [s for s in self.supplement_protocol if "workout" in s.timing.lower()]
        evening_supps = [s for s in self.supplement_protocol if "evening" in s.timing.lower() or "bed" in s.timing.lower()]
        other_supps = [s for s in self.supplement_protocol if s not in morning_supps + workout_supps + evening_supps]
        
        if morning_supps:
            print(f"\n🌅 MORNING:")
            for supp in morning_supps:
                print(f"   • {supp.name}: {supp.dosage} - {supp.purpose}")
        
        if workout_supps:
            print(f"\n🏋️ WORKOUT RELATED:")
            for supp in workout_supps:
                print(f"   • {supp.name}: {supp.dosage} ({supp.timing}) - {supp.purpose}")
        
        if evening_supps:
            print(f"\n🌙 EVENING:")
            for supp in evening_supps:
                print(f"   • {supp.name}: {supp.dosage} - {supp.purpose}")
        
        if other_supps:
            print(f"\n📋 AS NEEDED:")
            for supp in other_supps:
                print(f"   • {supp.name}: {supp.dosage} ({supp.timing}) - {supp.purpose}")
    
    def log_daily_metrics(self, weight_kg: float = None, body_fat: float = None,
                         energy: int = None, sleep_hours: float = None,
                         sleep_quality: int = None, stress: int = None, notes: str = ""):
        """Log daily progress metrics"""
        today = str(datetime.date.today())
        
        if today not in self.daily_logs:
            self.daily_logs[today] = DailyLog(today)
        
        log = self.daily_logs[today]
        if weight_kg: log.weight_kg = weight_kg
        if body_fat: log.body_fat_percent = body_fat
        if energy: log.energy_level = energy
        if sleep_hours: log.sleep_hours = sleep_hours
        if sleep_quality: log.sleep_quality = sleep_quality
        if stress: log.stress_level = stress
        if notes: log.notes = notes
        
        print(f"📝 Daily metrics logged for {today}")
        
        # Update current weight for macro calculations
        if weight_kg:
            self.current_weight = weight_kg
            print(f"⚖️ Weight updated: {weight_kg}kg")
    
    def progress_summary(self, days: int = 7):
        """Display progress summary for last N days"""
        recent_dates = sorted(self.daily_logs.keys())[-days:]
        
        if not recent_dates:
            print("📊 No progress data logged yet")
            return
        
        print(f"\n📈 PROGRESS SUMMARY - LAST {days} DAYS")
        print("=" * 50)
        
        weights = [self.daily_logs[d].weight_kg for d in recent_dates 
                  if self.daily_logs[d].weight_kg]
        energies = [self.daily_logs[d].energy_level for d in recent_dates 
                   if self.daily_logs[d].energy_level]
        sleep_hours = [self.daily_logs[d].sleep_hours for d in recent_dates 
                      if self.daily_logs[d].sleep_hours]
        
        if weights:
            weight_change = weights[-1] - weights[0] if len(weights) > 1 else 0
            print(f"⚖️ Weight: {weights[-1]:.1f}kg (Δ{weight_change:+.1f}kg)")
            
        if energies:
            avg_energy = sum(energies) / len(energies)
            print(f"⚡ Average Energy: {avg_energy:.1f}/10")
            
        if sleep_hours:
            avg_sleep = sum(sleep_hours) / len(sleep_hours)
            print(f"😴 Average Sleep: {avg_sleep:.1f} hours")
        
        # Progress toward goal
        if weights:
            remaining = weights[-1] - self.target_weight
            print(f"🎯 Goal Progress: {remaining:.1f}kg remaining to target")
            
        print(f"\n📅 Logged Days: {len(recent_dates)}/{days}")
    
    def meal_prep_shopping_list(self, days: int = 7):
        """Generate shopping list for meal prep"""
        phase_key = f"Phase {self.current_phase.name[0]}"
        meals = self.meal_templates.get(phase_key, [])
        
        all_foods = []
        for meal in meals:
            all_foods.extend(meal.foods)
        
        # Count occurrences and multiply by days
        food_counts = {}
        for food in all_foods:
            if food in food_counts:
                food_counts[food] += 1
            else:
                food_counts[food] = 1
        
        print(f"\n🛒 SHOPPING LIST - {days} DAYS ({phase_key})")
        print("=" * 50)
        
        # Group by category
        proteins = ["chicken", "fish", "eggs", "whey protein", "milk"]
        carbs = ["rice", "bread", "sweet potato", "banana", "apple", "oatmeal"]
        vegetables = ["salad", "vegetables", "spinach", "tomato"]
        others = ["ghee", "oil", "coffee", "tea", "almonds", "nuts"]
        
        categories = {
            "🥩 PROTEINS": proteins,
            "🍞 CARBOHYDRATES": carbs, 
            "🥬 VEGETABLES": vegetables,
            "🧈 FATS & OTHERS": others
        }
        
        for category, items in categories.items():
            print(f"\n{category}:")
            for food, count in food_counts.items():
                if any(item in food.lower() for item in items):
                    weekly_amount = count * days
                    print(f"   • {food}: {weekly_amount} servings")

# Example usage and demonstration
if __name__ == "__main__":
    # Create nutrition tracker
    tracker = NutritionTracker(Phase.FOUNDATION)
    
    print("🥗 COMPREHENSIVE NUTRITION & PROGRESS TRACKER 📊")
    print("Supports Hindu dietary preferences with complete macro tracking")
    
    # Display current targets
    tracker.display_daily_targets()
    
    # Show meal plan
    tracker.display_meal_plan()
    
    # Show supplements
    tracker.display_supplement_protocol()
    
    # Show shopping list
    tracker.meal_prep_shopping_list()
    
    print("\n" + "="*60)
    print("📱 HOW TO USE THIS TRACKER:")
    print("="*60)
    print("1. Daily logging: tracker.log_daily_metrics(weight=92.5, energy=8, sleep_hours=7)")
    print("2. Progress view: tracker.progress_summary(days=14)")
    print("3. Change phase: tracker.current_phase = Phase.STRENGTH")
    print("4. Shopping list: tracker.meal_prep_shopping_list(days=7)")
    
    print("\n🎯 PHASE PROGRESSION:")
    print("Phase 1 (Weeks 1-12): Fat Loss Focus - 2,100 kcal")
    print("Phase 2 (Weeks 13-24): Muscle Building - 2,400 kcal")
    print("Phase 3 (Weeks 25-36): Endurance Training - 2,700 kcal")
    print("Phase 4 (Weeks 37-44): Peak Performance - 2,900 kcal")
    
    print("\n💪 Ready to fuel your transformation journey!")
