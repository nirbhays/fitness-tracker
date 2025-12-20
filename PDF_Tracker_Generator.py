#!/usr/bin/env python3
"""
COMPREHENSIVE PDF FITNESS TRACKER GENERATOR
🏔️ Creates professional PDF workout trackers for all 4 phases 📊

Generates beautiful, printable PDF trackers with:
- Phase-specific workout plans
- Nutrition guidelines
- Progress tracking sheets
- Milestone charts
- Exercise illustrations (text-based)
"""

import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import Image as ReportLabImage
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
import io
import os

class FitnessTrackerPDFGenerator:
    def __init__(self):
        self.doc = None
        self.story = []
        self.styles = getSampleStyleSheet()
        self.custom_styles = self._create_custom_styles()
        
    def _create_custom_styles(self):
        """Create custom paragraph styles"""
        styles = {}
        
        # Title style
        styles['CustomTitle'] = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#2E86AB')
        )
        
        # Phase header style
        styles['PhaseHeader'] = ParagraphStyle(
            'PhaseHeader',
            parent=self.styles['Heading2'],
            fontSize=18,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#A23B72'),
            backColor=colors.HexColor('#F3F7FF')
        )
        
        # Exercise style
        styles['Exercise'] = ParagraphStyle(
            'Exercise',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=8,
            leftIndent=20
        )
        
        # Nutrition style
        styles['Nutrition'] = ParagraphStyle(
            'Nutrition',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            textColor=colors.HexColor('#2D5016')
        )
        
        return styles
    
    def create_cover_page(self):
        """Create an attractive cover page"""
        # Main title
        title = Paragraph("🏔️ 9-MONTH FITNESS TRANSFORMATION 🎒", self.custom_styles['CustomTitle'])
        self.story.append(title)
        self.story.append(Spacer(1, 30))
        
        # Subtitle
        subtitle = Paragraph("4-Day Workout & Nutrition Tracking System", self.styles['Heading3'])
        subtitle.alignment = TA_CENTER
        self.story.append(subtitle)
        self.story.append(Spacer(1, 20))
        
        # Goals section
        goals_text = """
        <b>PRIMARY GOALS:</b><br/>
        • Fat Loss: 15kg target (93kg → 78kg)<br/>
        • Mountain Expedition Preparation<br/>
        • Aesthetic Muscle Development<br/>
        • Joint Health & Injury Prevention<br/>
        <br/>
        <b>PROGRAM DURATION:</b> 39 weeks (9 months)<br/>
        <b>TRAINING SCHEDULE:</b> 4 workout days, 3 rest days per week<br/>
        <b>DIETARY APPROACH:</b> Hindu diet compliant<br/>
        <b>TRAINING STYLE:</b> Progressive 4-phase system
        """
        goals = Paragraph(goals_text, self.styles['Normal'])
        self.story.append(goals)
        self.story.append(Spacer(1, 30))
        
        # Phase overview table
        phase_data = [
            ['Phase', 'Weeks', 'Focus', 'Calories/Day'],
            ['Phase 1: Foundation', '1-10', 'Fat Loss & Movement Quality', '2,100 kcal'],
            ['Phase 2: Strength', '11-20', 'Muscle Building & Aesthetics', '2,400 kcal'],
            ['Phase 3: Endurance', '21-32', 'Hiking Prep & Altitude', '2,700 kcal'],
            ['Phase 4: Peak', '33-39', 'Expedition Readiness', '2,900 kcal']
        ]
        
        phase_table = Table(phase_data, colWidths=[1.5*inch, 1*inch, 2.2*inch, 1.3*inch])
        phase_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E86AB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9FA')),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
        ]))
        
        self.story.append(phase_table)
        self.story.append(Spacer(1, 30))
        
        # Program features
        features_text = """
        <b>🎯 KEY FEATURES:</b><br/>
        ✓ Progressive 4-phase periodization<br/>
        ✓ Joint-friendly exercise modifications<br/>
        ✓ Hindu diet compliant meal plans<br/>
        ✓ Aesthetic muscle development focus<br/>
        ✓ Mountain hiking preparation<br/>
        ✓ Comprehensive progress tracking<br/>
        ✓ Supplement protocol included<br/>
        ✓ Milestone celebration system<br/>
        <br/>
        <b>📅 Start Date:</b> _______________<br/>
        <b>🏔️ Target Expedition Date:</b> _______________<br/>
        <b>⚖️ Starting Weight:</b> _______________<br/>
        <b>🎯 Target Weight:</b> _______________
        """
        features = Paragraph(features_text, self.styles['Normal'])
        self.story.append(features)
        
        self.story.append(PageBreak())
    
    def create_phase_tracker(self, phase_num, phase_name, weeks, focus, workouts_data):
        """Create a detailed phase tracker page"""
        # Phase header
        header_text = f"📋 PHASE {phase_num}: {phase_name.upper()}"
        header = Paragraph(header_text, self.custom_styles['PhaseHeader'])
        self.story.append(header)
        self.story.append(Spacer(1, 20))
        
        # Phase info
        info_text = f"""
        <b>Duration:</b> Weeks {weeks}<br/>
        <b>Primary Focus:</b> {focus}<br/>
        <b>Training Frequency:</b> 4 days per week<br/>
        <b>Rest Days:</b> 3 days per week<br/>
        <b>Session Duration:</b> 60-90 minutes
        """
        info = Paragraph(info_text, self.styles['Normal'])
        self.story.append(info)
        self.story.append(Spacer(1, 15))
        
        # Weekly workout schedule
        workout_header = Paragraph("<b>📅 WEEKLY WORKOUT SCHEDULE</b>", self.styles['Heading4'])
        self.story.append(workout_header)
        self.story.append(Spacer(1, 10))
        
        # Create workout table
        workout_table_data = [['Day', 'Focus', 'Key Exercises', '✓ Done']]
        
        for day, details in workouts_data.items():
            workout_table_data.append([
                day,
                details['focus'],
                details['key_exercises'],
                '☐'
            ])
        
        workout_table = Table(workout_table_data, colWidths=[0.8*inch, 1.5*inch, 3*inch, 0.7*inch])
        workout_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#A23B72')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        self.story.append(workout_table)
        self.story.append(Spacer(1, 20))
        
        # Progress tracking section
        progress_header = Paragraph("<b>📊 WEEKLY PROGRESS TRACKING</b>", self.styles['Heading4'])
        self.story.append(progress_header)
        self.story.append(Spacer(1, 10))
        
        # Progress table
        progress_data = [
            ['Week', 'Weight (kg)', 'Body Fat %', 'Energy (1-10)', 'Sleep Hours', 'Notes'],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
        ]
        
        progress_table = Table(progress_data, colWidths=[0.7*inch, 0.9*inch, 0.9*inch, 1*inch, 1*inch, 1.5*inch])
        progress_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E86AB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
        ]))
        
        self.story.append(progress_table)
        self.story.append(Spacer(1, 15))
        
        # Weekly mood tracker
        mood_text = """
        <b>😊 WEEKLY MOOD TRACKER:</b><br/>
        Circle your dominant mood each day: 😤 💪 😊 😐 😴<br/>
        Mon: 😤 💪 😊 😐 😴 | Tue: 😤 💪 😊 😐 😴 | Wed: 😤 💪 😊 😐 😴<br/>
        Thu: 😤 💪 😊 😐 😴 | Fri: 😤 💪 😊 😐 😴 | Sat: 😤 💪 😊 😐 😴 | Sun: 😤 💪 😊 😐 😴
        """
        mood = Paragraph(mood_text, self.styles['Normal'])
        self.story.append(mood)
        self.story.append(Spacer(1, 15))
        
        # Phase-specific tips
        tips_text = self._get_phase_tips(phase_num)
        tips = Paragraph(f"<b>💡 PHASE {phase_num} SUCCESS TIPS:</b><br/>{tips_text}", self.styles['Normal'])
        self.story.append(tips)
        
        self.story.append(PageBreak())
    
    def _get_phase_tips(self, phase_num):
        """Get phase-specific success tips"""
        tips = {
            1: """
            • Focus on form over weight - build movement quality<br/>
            • Track your meals consistently for fat loss<br/>
            • Start with bodyweight/light weights<br/>
            • Prioritize 7-8 hours of sleep<br/>
            • Take progress photos weekly<br/>
            • Listen to your body - modify if knee/back pain occurs
            """,
            2: """
            • Progressive overload is key - add weight/reps weekly<br/>
            • Track personal records (PRs) for motivation<br/>
            • Increase protein intake to 2g/kg bodyweight<br/>
            • Start pack training with light weight (8-10kg)<br/>
            • Focus on aesthetic exercises for muscle definition<br/>
            • Deload every 4th week for recovery
            """,
            3: """
            • Build hiking endurance gradually<br/>
            • Practice breathing exercises daily<br/>
            • Increase pack weight to 15-20kg<br/>
            • Simulate hiking conditions (terrain, weather)<br/>
            • Maintain strength while building cardio<br/>
            • Test gear and equipment regularly
            """,
            4: """
            • Practice back-to-back hiking days<br/>
            • Complete expedition gear testing<br/>
            • Focus on mental preparation<br/>
            • Taper training 2 weeks before expedition<br/>
            • Practice emergency protocols<br/>
            • Ensure complete readiness checklist
            """
        }
        return tips.get(phase_num, "")
    
    def create_nutrition_guide(self):
        """Create comprehensive nutrition guide"""
        # Nutrition header
        header = Paragraph("🥗 HINDU DIET NUTRITION GUIDE", self.custom_styles['PhaseHeader'])
        self.story.append(header)
        self.story.append(Spacer(1, 20))
        
        # Introduction
        intro_text = """
        This nutrition plan is designed to be Hindu diet compliant while supporting your
        transformation goals. The plan includes chicken, fish, eggs, dairy, and vegetables
        while excluding beef and pork.
        """
        intro = Paragraph(intro_text, self.styles['Normal'])
        self.story.append(intro)
        self.story.append(Spacer(1, 15))
        
        # Macro targets by phase
        macro_header = Paragraph("<b>📊 MACRO TARGETS BY PHASE</b>", self.styles['Heading4'])
        self.story.append(macro_header)
        self.story.append(Spacer(1, 10))
        
        macro_data = [
            ['Phase', 'Calories', 'Protein %', 'Carbs %', 'Fat %', 'Focus'],
            ['Phase 1', '2,100', '35%', '30%', '35%', 'Fat Loss'],
            ['Phase 2', '2,400', '30%', '40%', '30%', 'Muscle Building'],
            ['Phase 3', '2,700', '25%', '45%', '30%', 'Endurance'],
            ['Phase 4', '2,900', '25%', '50%', '25%', 'Performance']
        ]
        
        macro_table = Table(macro_data, colWidths=[1*inch, 1*inch, 1*inch, 1*inch, 1*inch, 1*inch])
        macro_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2D5016')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F0F8E8')])
        ]))
        
        self.story.append(macro_table)
        self.story.append(Spacer(1, 20))
        
        # Sample meal plan
        meal_header = Paragraph("<b>🍽️ SAMPLE DAILY MEAL PLAN (PHASE 1)</b>", self.styles['Heading4'])
        self.story.append(meal_header)
        self.story.append(Spacer(1, 10))
        
        meal_data = [
            ['Time', 'Meal', 'Foods', 'Calories'],
            ['6:00 AM', 'Pre-Workout', 'Black coffee, 5g BCAA', '50'],
            ['8:00 AM', 'Breakfast', '2-egg omelette, 2 slices ezekiel bread, ghee', '400'],
            ['10:30 AM', 'Mid-Morning', '1 apple, 15g almonds', '200'],
            ['1:00 PM', 'Lunch', '150g chicken, large salad, 2 boiled eggs', '500'],
            ['4:00 PM', 'Pre-Workout', '1 banana, black coffee', '150'],
            ['7:00 PM', 'Post-Workout', '40g whey protein shake', '160'],
            ['8:00 PM', 'Dinner', '100g rice, 150g fish curry, vegetables', '600'],
            ['9:30 PM', 'Evening', 'Green tea', '0']
        ]
        
        meal_table = Table(meal_data, colWidths=[1*inch, 1.2*inch, 2.8*inch, 1*inch])
        meal_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2D5016')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (3, 0), (3, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6)
        ]))
        
        self.story.append(meal_table)
        self.story.append(Spacer(1, 20))
        
        # Supplement protocol
        supp_header = Paragraph("<b>💊 SUPPLEMENT PROTOCOL</b>", self.styles['Heading4'])
        self.story.append(supp_header)
        self.story.append(Spacer(1, 10))
        
        supp_text = """
        <b>🌅 MORNING:</b><br/>
        • Multivitamin: 2 tablets<br/>
        • Vitamin D3: 2,000-4,000 IU<br/>
        • Iron + Vitamin C: 18mg Fe + 100mg C (empty stomach)<br/>
        <br/>
        <b>🏋️ WORKOUT RELATED:</b><br/>
        • Pre-workout: Black coffee + 5g BCAA<br/>
        • Intra-workout: 10g BCAA in 1.5L water<br/>
        • Post-workout: 25-50g whey protein<br/>
        • Post-workout: 5g creatine<br/>
        <br/>
        <b>🌙 EVENING:</b><br/>
        • Multivitamin: 2 tablets<br/>
        • Ashwagandha: 300mg (TSH/testosterone support)<br/>
        • Magnesium: 400mg (before bed for sleep)<br/>
        <br/>
        <b>📋 AS NEEDED:</b><br/>
        • Omega-3: 2g EPA/DHA (with meals)<br/>
        • Electrolytes: During long hikes
        """
        supp = Paragraph(supp_text, self.styles['Normal'])
        self.story.append(supp)
        
        self.story.append(PageBreak())
    
    def create_progress_chart_page(self):
        """Create a progress tracking chart page"""
        # Progress header
        header = Paragraph("📈 PROGRESS TRACKING CHARTS", self.custom_styles['PhaseHeader'])
        self.story.append(header)
        self.story.append(Spacer(1, 20))
        
        # Weight loss chart template
        weight_header = Paragraph("<b>⚖️ WEIGHT LOSS PROGRESS CHART</b>", self.styles['Heading4'])
        self.story.append(weight_header)
        self.story.append(Spacer(1, 10))
        
        # Create weight tracking table
        weeks = list(range(1, 40, 4))  # Every 4 weeks for 39 weeks
        weight_data = [['Week'] + [str(w) for w in weeks]]
        weight_data.append(['Weight (kg)'] + [''] * len(weeks))
        weight_data.append(['Body Fat %'] + [''] * len(weeks))
        
        weight_table = Table(weight_data, colWidths=[1*inch] + [0.5*inch] * len(weeks))
        weight_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E86AB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#A23B72')),
            ('TEXTCOLOR', (0, 1), (0, -1), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (1, 1), (-1, -1), colors.white)
        ]))
        
        self.story.append(weight_table)
        self.story.append(Spacer(1, 20))
        
        # Milestone celebrations
        milestone_header = Paragraph("<b>🏆 MILESTONE CELEBRATIONS</b>", self.styles['Heading4'])
        self.story.append(milestone_header)
        self.story.append(Spacer(1, 10))
        
        milestone_data = [
            ['Milestone', 'Target', 'Date Achieved', 'Reward/Celebration'],
            ['2.5kg Lost', '90.5kg', '', ''],
            ['5.0kg Lost', '88.0kg', '', ''],
            ['7.5kg Lost', '85.5kg', '', ''],
            ['10.0kg Lost', '83.0kg', '', ''],
            ['12.5kg Lost', '80.5kg', '', ''],
            ['15.0kg Lost', '78.0kg', '', '🎉 GOAL ACHIEVED!']
        ]
        
        milestone_table = Table(milestone_data, colWidths=[1.5*inch, 1*inch, 1.5*inch, 2*inch])
        milestone_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#B8860B')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FFFACD')])
        ]))
        
        self.story.append(milestone_table)
        self.story.append(Spacer(1, 20))
        
        # Body measurements tracking
        measurements_header = Paragraph("<b>📏 BODY MEASUREMENTS TRACKING</b>", self.styles['Heading4'])
        self.story.append(measurements_header)
        self.story.append(Spacer(1, 10))
        
        measurements_data = [
            ['Date', 'Weight', 'Waist', 'Chest', 'Arms', 'Thighs', 'Notes'],
            ['Start:', '', '', '', '', '', ''],
            ['Week 4:', '', '', '', '', '', ''],
            ['Week 8:', '', '', '', '', '', ''],
            ['Week 12:', '', '', '', '', '', ''],
            ['Week 16:', '', '', '', '', '', ''],
            ['Week 20:', '', '', '', '', '', ''],
            ['Week 24:', '', '', '', '', '', ''],
            ['Week 28:', '', '', '', '', '', ''],
            ['Week 32:', '', '', '', '', '', ''],
            ['Week 36:', '', '', '', '', '', ''],
            ['Week 39:', '', '', '', '', '', '']
        ]
        
        measurements_table = Table(measurements_data, colWidths=[0.8*inch, 0.7*inch, 0.7*inch, 0.7*inch, 0.7*inch, 0.7*inch, 1.7*inch])
        measurements_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E86AB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
        ]))
        
        self.story.append(measurements_table)
        self.story.append(PageBreak())
    
    def create_expedition_readiness_page(self):
        """Create expedition readiness checklist"""
        # Header
        header = Paragraph("🏔️ EXPEDITION READINESS CHECKLIST", self.custom_styles['PhaseHeader'])
        self.story.append(header)
        self.story.append(Spacer(1, 20))
        
        # Introduction
        intro_text = """
        Use this checklist to ensure you're completely prepared for your mountain expedition.
        Complete this assessment 2 weeks before your departure date.
        """
        intro = Paragraph(intro_text, self.styles['Normal'])
        self.story.append(intro)
        self.story.append(Spacer(1, 15))
        
        # Physical conditioning checklist
        physical_header = Paragraph("<b>💪 PHYSICAL CONDITIONING</b>", self.styles['Heading4'])
        self.story.append(physical_header)
        self.story.append(Spacer(1, 10))
        
        physical_data = [
            ['Requirement', 'Target', 'Achieved?', 'Notes'],
            ['6+ hour hiking capability', 'Complete without excessive fatigue', '☐', ''],
            ['20kg pack comfort', 'Carry for 4+ hours comfortably', '☐', ''],
            ['Back-to-back day recovery', '<2 point energy drop on day 2', '☐', ''],
            ['Zero pain/injury issues', 'No knee, back, or joint problems', '☐', ''],
            ['Cardiovascular fitness', 'Conversation pace at altitude', '☐', ''],
            ['Strength maintenance', 'No loss from Phase 2 gains', '☐', '']
        ]
        
        physical_table = Table(physical_data, colWidths=[2*inch, 2*inch, 1*inch, 1*inch])
        physical_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B4513')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        self.story.append(physical_table)
        self.story.append(Spacer(1, 15))
        
        # Technical skills checklist
        technical_header = Paragraph("<b>🧭 TECHNICAL SKILLS</b>", self.styles['Heading4'])
        self.story.append(technical_header)
        self.story.append(Spacer(1, 10))
        
        technical_data = [
            ['Skill', 'Requirement', 'Achieved?', 'Notes'],
            ['Navigation proficiency', 'Map & compass/GPS skills', '☐', ''],
            ['Gear familiarity', 'Know all equipment functions', '☐', ''],
            ['Emergency protocols', 'First aid, evacuation plans', '☐', ''],
            ['Weather assessment', 'Can read conditions/forecasts', '☐', ''],
            ['Route knowledge', 'Familiar with planned route', '☐', ''],
            ['Risk management', 'Identify and mitigate hazards', '☐', '']
        ]
        
        technical_table = Table(technical_data, colWidths=[2*inch, 2*inch, 1*inch, 1*inch])
        technical_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2F4F4F')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        self.story.append(technical_table)
        self.story.append(Spacer(1, 15))
        
        # Gear checklist
        gear_header = Paragraph("<b>🎒 GEAR & EQUIPMENT</b>", self.styles['Heading4'])
        self.story.append(gear_header)
        self.story.append(Spacer(1, 10))
        
        gear_data = [
            ['Item', 'Requirement', 'Tested?', 'Notes'],
            ['Hiking boots', 'Broken in, comfortable, waterproof', '☐', ''],
            ['Backpack', 'Properly fitted, comfortable with load', '☐', ''],
            ['Clothing system', 'Layering tested in conditions', '☐', ''],
            ['Shelter system', 'Tent/tarp, sleeping bag rated', '☐', ''],
            ['Navigation tools', 'GPS, map, compass, backup', '☐', ''],
            ['Emergency gear', 'First aid, whistle, headlamp', '☐', ''],
            ['Nutrition/hydration', 'Water filter, food, electrolytes', '☐', '']
        ]
        
        gear_table = Table(gear_data, colWidths=[1.5*inch, 2.5*inch, 1*inch, 1*inch])
        gear_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#556B2F')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (2, 0), (2, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8)
        ]))
        
        self.story.append(gear_table)
        self.story.append(Spacer(1, 20))
        
        # Final assessment
        final_text = """
        <b>🎯 FINAL READINESS ASSESSMENT:</b><br/>
        <br/>
        Overall readiness score: ___/20 items completed<br/>
        <br/>
        <b>If you scored:</b><br/>
        • 18-20: You're ready for the expedition! 🎉<br/>
        • 15-17: Address remaining items before departure<br/>
        • <15: More preparation needed - consider delaying<br/>
        <br/>
        <b>📅 Final preparation date:</b> _______________<br/>
        <b>🏔️ Expedition departure date:</b> _______________<br/>
        <br/>
        <i>Remember: It's better to be over-prepared than under-prepared for mountain adventures!</i>
        """
        final = Paragraph(final_text, self.styles['Normal'])
        self.story.append(final)
        
        self.story.append(PageBreak())
    
    def generate_pdf(self, filename="Complete_Fitness_Tracker.pdf"):
        """Generate the complete PDF tracker"""
        self.doc = SimpleDocTemplate(filename, pagesize=A4,
                                   rightMargin=72, leftMargin=72,
                                   topMargin=72, bottomMargin=18)
        
        # Create cover page
        self.create_cover_page()
        
        # Create phase trackers
        phase_data = {
            1: {
                'name': 'Foundation & Fat Loss',
                'weeks': '1-10',
                'focus': 'Movement quality, fat loss, joint health',
                'workouts': {
                    'Monday': {
                        'focus': 'Lower Body Strength',
                        'key_exercises': 'Goblet Squats, RDL, Lunges, Calf Raises, Planks'
                    },
                    'Tuesday': {
                        'focus': 'Upper Body + Core',
                        'key_exercises': 'Lat Pulldowns, Incline Press, Rows, Lateral Raises'
                    },
                    'Wednesday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Thursday': {
                        'focus': 'Full Body Circuit',
                        'key_exercises': 'Push-ups, Bodyweight Squats, Pike Push-ups'
                    },
                    'Friday': {
                        'focus': 'HIIT + Cardio',
                        'key_exercises': 'Incline Walk, Bike Intervals, Core Circuit'
                    },
                    'Saturday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Sunday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    }
                }
            },
            2: {
                'name': 'Strength & Hypertrophy',
                'weeks': '11-20',
                'focus': 'Muscle building, strength gains, aesthetic development',
                'workouts': {
                    'Monday': {
                        'focus': 'Lower Power',
                        'key_exercises': 'Back Squats, RDL, Bulgarian Split Squats, Hip Thrusts'
                    },
                    'Tuesday': {
                        'focus': 'Upper Power',
                        'key_exercises': 'Pull-ups, Incline Barbell Press, Bent-over Rows'
                    },
                    'Wednesday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Thursday': {
                        'focus': 'Unilateral & Prehab',
                        'key_exercises': 'Single-leg RDL, Band Walks, Pallof Press'
                    },
                    'Friday': {
                        'focus': 'Hypertrophy Circuit',
                        'key_exercises': 'High-rep compound movements, Farmer\'s Walks'
                    },
                    'Saturday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Sunday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    }
                }
            },
            3: {
                'name': 'Endurance & Altitude Prep',
                'weeks': '21-32',
                'focus': 'Aerobic capacity, hiking-specific conditioning',
                'workouts': {
                    'Monday': {
                        'focus': 'Hiking Simulation',
                        'key_exercises': 'Incline Treadmill, Weighted Step-ups'
                    },
                    'Tuesday': {
                        'focus': 'Strength Maintenance',
                        'key_exercises': 'Trap Bar Deadlift, Incline Press, Cable Rows'
                    },
                    'Wednesday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Thursday': {
                        'focus': 'Strength + Plyometrics',
                        'key_exercises': 'KB Swings, Box Step-ups, Med Ball Slams'
                    },
                    'Friday': {
                        'focus': 'Long Hike Training',
                        'key_exercises': '3-4 hour hike with 15-20kg pack'
                    },
                    'Saturday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Sunday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    }
                }
            },
            4: {
                'name': 'Peak Hike Simulation',
                'weeks': '33-39',
                'focus': 'Expedition readiness, peak performance',
                'workouts': {
                    'Monday': {
                        'focus': 'Back-to-Back Hike Day 1',
                        'key_exercises': '4-5 hour hike, Navigation Practice, Gear Testing'
                    },
                    'Tuesday': {
                        'focus': 'Back-to-Back Hike Day 2',
                        'key_exercises': '4-5 hour hike, Fatigue Management, Skills Practice'
                    },
                    'Wednesday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Thursday': {
                        'focus': 'Strength Endurance',
                        'key_exercises': 'High-rep Circuit, Functional Movements'
                    },
                    'Friday': {
                        'focus': 'Peak Simulation Hike',
                        'key_exercises': '6 hour expedition simulation'
                    },
                    'Saturday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    },
                    'Sunday': {
                        'focus': 'REST DAY',
                        'key_exercises': 'Complete rest and recovery'
                    }
                }
            }
        }
        
        for phase_num, data in phase_data.items():
            self.create_phase_tracker(
                phase_num, 
                data['name'], 
                data['weeks'], 
                data['focus'], 
                data['workouts']
            )
        
        # Create nutrition guide
        self.create_nutrition_guide()
        
        # Create progress tracking pages
        self.create_progress_chart_page()
        
        # Create expedition readiness page
        self.create_expedition_readiness_page()
        
        # Build PDF
        self.doc.build(self.story)
        print(f"✅ PDF tracker generated: {filename}")
        return filename

# Main execution
if __name__ == "__main__":
    print("🏔️ GENERATING COMPREHENSIVE FITNESS TRACKER PDF 📊")
    print("=" * 60)
    
    generator = FitnessTrackerPDFGenerator()
    
    # Generate the complete PDF
    pdf_filename = generator.generate_pdf("Complete_Fitness_Transformation_Tracker.pdf")
    
    print(f"\n🎉 SUCCESS! Your comprehensive fitness tracker has been generated!")
    print(f"📁 File: {pdf_filename}")
    print(f"📄 Pages: Cover + 4 Phase Trackers + Nutrition Guide + Progress Charts + Expedition Readiness")
    print(f"\n💡 This PDF includes:")
    print("• Complete 44-week program overview")
    print("• Detailed workout schedules for all 4 phases")
    print("• Hindu diet nutrition guidelines")
    print("• Progress tracking charts and milestone celebrations")
    print("• Expedition readiness checklist")
    print("• Weekly mood and energy tracking")
    print("• Supplement protocol")
    print("• Body measurement tracking")
    print("\n🏔️ Ready to start your transformation journey! 💪")
    print("Print this PDF and use it as your complete fitness companion!")
