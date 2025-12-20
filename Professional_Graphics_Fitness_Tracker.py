#!/usr/bin/env python3
"""
PROFESSIONAL GRAPHICS FITNESS TRACKER
====================================

Professional business-grade design with maximum graphics
Based on:
- Fortune 500 Company Report Design
- Medical Professional Documentation
- Corporate Wellness Program Standards
- Executive Presentation Guidelines
- Healthcare Industry Best Practices
- Professional Sports Science Reports

Professional + Graphics: Business-ready with visual excellence
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Wedge, Polygon, Arc
import numpy as np
from datetime import datetime, timedelta
import os
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects
from matplotlib import font_manager

plt.switch_backend('Agg')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Liberation Sans', 'Arial', 'Helvetica']

class ProfessionalGraphicsFitnessTracker:
    """Professional graphics fitness tracker with business-grade design"""
    
    def __init__(self):
        self.setup_professional_colors()
        self.setup_corporate_design_system()
        self.create_professional_icons()
        
    def setup_professional_colors(self):
        """Professional corporate color palette"""
        
        self.colors = {
            # Primary corporate colors
            'corporate_blue': '#1E3A8A',       # Trust, stability
            'executive_navy': '#1E293B',       # Authority, professionalism
            'professional_teal': '#0F766E',    # Growth, balance
            'business_green': '#166534',       # Success, health
            
            # Secondary professional colors
            'premium_gold': '#B45309',         # Achievement, excellence
            'corporate_gray': '#374151',       # Neutral, sophisticated
            'charcoal': '#1F2937',            # Text, contrast
            'slate': '#475569',               # Secondary text
            
            # Functional colors
            'success_green': '#16A34A',        # Positive outcomes
            'warning_amber': '#D97706',        # Caution, attention
            'info_blue': '#2563EB',           # Information, guidance
            'accent_purple': '#7C3AED',       # Highlights, emphasis
            
            # Background and surface colors
            'white': '#FFFFFF',               # Primary background
            'light_gray': '#F8FAFC',          # Secondary background
            'border_gray': '#E2E8F0',         # Borders, dividers
            'surface_white': '#FEFEFE',       # Card surfaces
            
            # Professional gradients
            'gradient_blue_start': '#3B82F6',
            'gradient_blue_end': '#1E40AF',
            'gradient_teal_start': '#14B8A6',
            'gradient_teal_end': '#0F766E',
        }
        
        self.create_professional_gradients()
        
    def create_professional_gradients(self):
        """Create sophisticated professional gradients"""
        
        # Corporate blue gradient
        blue_colors = [self.colors['gradient_blue_start'], self.colors['gradient_blue_end']]
        self.corporate_gradient = LinearSegmentedColormap.from_list('corporate', blue_colors)
        
        # Professional teal gradient
        teal_colors = [self.colors['gradient_teal_start'], self.colors['gradient_teal_end']]
        self.professional_gradient = LinearSegmentedColormap.from_list('professional', teal_colors)
        
        # Success gradient
        success_colors = [self.colors['business_green'], self.colors['success_green']]
        self.success_gradient = LinearSegmentedColormap.from_list('success', success_colors)
        
    def setup_corporate_design_system(self):
        """Setup professional corporate design system"""
        
        self.typography = {
            'title': {'size': 20, 'weight': '700', 'color': self.colors['executive_navy']},
            'subtitle': {'size': 14, 'weight': '600', 'color': self.colors['corporate_gray']},
            'header': {'size': 11, 'weight': '600', 'color': self.colors['white']},
            'body': {'size': 9, 'weight': '400', 'color': self.colors['charcoal']},
            'caption': {'size': 8, 'weight': '400', 'color': self.colors['slate']},
            'label': {'size': 9, 'weight': '500', 'color': self.colors['executive_navy']},
            'emphasis': {'size': 10, 'weight': '600', 'color': self.colors['corporate_blue']},
        }
        
        self.spacing = {
            'xs': 0.005,
            'sm': 0.01,
            'md': 0.015,
            'lg': 0.02,
            'xl': 0.03,
        }
        
        self.borders = {
            'radius': 0.008,
            'width_thin': 1,
            'width_medium': 1.5,
            'width_thick': 2,
        }
        
    def create_professional_icons(self):
        """Create professional vector icons"""
        
        self.icons = {
            'strength': self.create_professional_strength_icon,
            'cardio': self.create_professional_cardio_icon,
            'flexibility': self.create_professional_flexibility_icon,
            'core': self.create_professional_core_icon,
            'warmup': self.create_professional_warmup_icon,
            'achievement': self.create_professional_achievement_icon,
            'progress': self.create_professional_progress_icon,
            'time': self.create_professional_time_icon,
            'metrics': self.create_professional_metrics_icon,
        }
        
    def create_professional_strength_icon(self, ax, x, y, size=0.015, color='#1E3A8A'):
        """Create professional strength training icon"""
        
        # Modern dumbbell design
        # Center bar
        bar = Rectangle((x-size*0.4, y-size*0.08), size*0.8, size*0.16,
                       facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(bar)
        
        # Left weight plate
        left_plate = FancyBboxPatch((x-size*0.5, y-size*0.2), size*0.2, size*0.4,
                                  boxstyle=f"round,pad={self.spacing['xs']}",
                                  facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(left_plate)
        
        # Right weight plate
        right_plate = FancyBboxPatch((x+size*0.3, y-size*0.2), size*0.2, size*0.4,
                                   boxstyle=f"round,pad={self.spacing['xs']}",
                                   facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(right_plate)
        
        # Professional highlight
        highlight = Rectangle((x-size*0.35, y+size*0.05), size*0.7, size*0.03,
                            facecolor=self.colors['white'], alpha=0.3)
        ax.add_patch(highlight)
        
    def create_professional_cardio_icon(self, ax, x, y, size=0.015, color='#16A34A'):
        """Create professional cardio icon"""
        
        # Heart shape with professional styling
        t = np.linspace(0, 2*np.pi, 50)
        heart_x = size * 0.6 * (16 * np.sin(t)**3) / 20 + x
        heart_y = size * 0.6 * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) / 20 + y
        
        heart = Polygon(list(zip(heart_x, heart_y)), 
                       facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(heart)
        
        # Professional pulse line
        pulse_x = np.linspace(x-size*0.8, x+size*0.8, 100)
        pulse_y = y + size*0.6 + size*0.15 * np.sin(pulse_x * 20)
        ax.plot(pulse_x, pulse_y, color=color, linewidth=2, alpha=0.7)
        
    def create_professional_flexibility_icon(self, ax, x, y, size=0.015, color='#7C3AED'):
        """Create professional flexibility icon"""
        
        # Stylized yoga pose
        # Head
        head = Circle((x, y+size*0.35), size*0.12, 
                     facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(head)
        
        # Body (torso)
        torso = Rectangle((x-size*0.08, y-size*0.1), size*0.16, size*0.4,
                         facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(torso)
        
        # Arms in yoga position
        # Left arm
        left_arm = FancyBboxPatch((x-size*0.25, y+size*0.1), size*0.15, size*0.08,
                                boxstyle=f"round,pad={self.spacing['xs']}",
                                facecolor=color, alpha=0.8)
        ax.add_patch(left_arm)
        
        # Right arm
        right_arm = FancyBboxPatch((x+size*0.1, y+size*0.1), size*0.15, size*0.08,
                                 boxstyle=f"round,pad={self.spacing['xs']}",
                                 facecolor=color, alpha=0.8)
        ax.add_patch(right_arm)
        
    def create_professional_core_icon(self, ax, x, y, size=0.015, color='#D97706'):
        """Create professional core training icon"""
        
        # Stylized core/abs representation
        for i, y_offset in enumerate([-0.15, -0.05, 0.05, 0.15]):
            for j, x_offset in enumerate([-0.08, 0.08]):
                abs_segment = FancyBboxPatch((x + size*x_offset - size*0.06, y + size*y_offset - size*0.04),
                                           size*0.12, size*0.08,
                                           boxstyle=f"round,pad={self.spacing['xs']}",
                                           facecolor=color, 
                                           edgecolor=self.colors['border_gray'], 
                                           linewidth=1, alpha=0.9)
                ax.add_patch(abs_segment)
                
    def create_professional_warmup_icon(self, ax, x, y, size=0.015, color='#B45309'):
        """Create professional warmup icon"""
        
        # Professional arrow indicating movement/warmup
        # Arrow body
        arrow_body = Rectangle((x-size*0.3, y-size*0.05), size*0.5, size*0.1,
                             facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(arrow_body)
        
        # Arrow head
        arrow_head = Polygon([(x+size*0.2, y-size*0.15), 
                             (x+size*0.4, y), 
                             (x+size*0.2, y+size*0.15)],
                            facecolor=color, edgecolor=self.colors['border_gray'], linewidth=1)
        ax.add_patch(arrow_head)
        
        # Movement lines
        for i, offset in enumerate([0.1, 0.2, 0.3]):
            line_y = y + size*0.25
            ax.plot([x-size*offset, x-size*(offset-0.15)], [line_y, line_y], 
                   color=color, linewidth=1, alpha=0.6)
                   
    def create_professional_achievement_icon(self, ax, x, y, size=0.015, color='#B45309'):
        """Create professional achievement badge"""
        
        # Professional badge/award
        badge = Circle((x, y), size*0.8, 
                      facecolor=color, edgecolor=self.colors['border_gray'], linewidth=2)
        ax.add_patch(badge)
        
        # Inner design
        inner_circle = Circle((x, y), size*0.5, 
                            facecolor=self.colors['white'], alpha=0.9)
        ax.add_patch(inner_circle)
        
        # Award symbol
        star_angles = np.linspace(0, 2*np.pi, 6)
        star_x = x + size*0.3 * np.cos(star_angles)
        star_y = y + size*0.3 * np.sin(star_angles)
        
        star = Polygon(list(zip(star_x, star_y)), 
                      facecolor=color, alpha=0.8)
        ax.add_patch(star)
        
    def create_professional_progress_icon(self, ax, x, y, size=0.015, color='#2563EB'):
        """Create professional progress indicator"""
        
        # Progress circle
        progress_bg = Circle((x, y), size*0.8, 
                           facecolor='none', edgecolor=self.colors['border_gray'], linewidth=2)
        ax.add_patch(progress_bg)
        
        # Progress fill (3/4 complete)
        progress_fill = Wedge((x, y), size*0.8, 90, 360, 
                            facecolor=color, alpha=0.8)
        ax.add_patch(progress_fill)
        
        # Center dot
        center_dot = Circle((x, y), size*0.2, 
                          facecolor=self.colors['white'])
        ax.add_patch(center_dot)
        
    def create_professional_time_icon(self, ax, x, y, size=0.015, color='#0F766E'):
        """Create professional time/clock icon"""
        
        # Clock face
        clock_face = Circle((x, y), size*0.8, 
                          facecolor=self.colors['white'], 
                          edgecolor=color, linewidth=2)
        ax.add_patch(clock_face)
        
        # Clock hands
        # Hour hand
        ax.plot([x, x+size*0.3], [y, y+size*0.3], 
               color=color, linewidth=2)
        
        # Minute hand
        ax.plot([x, x+size*0.5], [y, y], 
               color=color, linewidth=1.5)
               
        # Center dot
        center = Circle((x, y), size*0.1, 
                       facecolor=color)
        ax.add_patch(center)
        
    def create_professional_metrics_icon(self, ax, x, y, size=0.015, color='#7C3AED'):
        """Create professional metrics/chart icon"""
        
        # Chart bars
        bar_heights = [0.3, 0.6, 0.4, 0.8]
        bar_width = size*0.15
        
        for i, height in enumerate(bar_heights):
            bar_x = x - size*0.4 + i*size*0.2
            bar = Rectangle((bar_x, y-size*0.4), bar_width, size*height*2,
                          facecolor=color, alpha=0.8)
            ax.add_patch(bar)
            
        # Chart base line
        ax.plot([x-size*0.5, x+size*0.3], [y-size*0.4, y-size*0.4], 
               color=self.colors['border_gray'], linewidth=1)
               
    def create_professional_header(self, ax, title, subtitle="", day_info=None):
        """Create professional business-grade header"""
        
        # Professional header background with subtle gradient
        header_height = 0.15
        
        # Subtle gradient background
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        ax.imshow(gradient, extent=[0, 1, 1-header_height, 1], aspect='auto', 
                 cmap=self.corporate_gradient, alpha=0.1)
                 
        # Header container with professional border
        header_container = FancyBboxPatch(
            (0.02, 1-header_height+0.01), 0.96, header_height-0.02,
            boxstyle=f"round,pad={self.spacing['sm']}",
            facecolor=self.colors['white'],
            edgecolor=self.colors['corporate_blue'],
            linewidth=2, alpha=0.95
        )
        ax.add_patch(header_container)
        
        # Professional logo/branding area
        self.add_professional_branding(ax)
        
        # Main title with professional styling
        title_text = ax.text(0.5, 0.94, title, 
                           fontsize=self.typography['title']['size'],
                           fontweight=self.typography['title']['weight'],
                           color=self.typography['title']['color'],
                           ha='center', va='center',
                           transform=ax.transAxes)
        
        # Subtitle with professional hierarchy
        if subtitle:
            ax.text(0.5, 0.90, subtitle, 
                   fontsize=self.typography['subtitle']['size'],
                   fontweight=self.typography['subtitle']['weight'],
                   color=self.typography['subtitle']['color'],
                   ha='center', va='center',
                   transform=ax.transAxes, style='italic')
        
        # Professional day indicator
        if day_info:
            self.create_professional_day_indicator(ax, day_info)
            
        # Header metadata
        self.add_professional_metadata(ax)
        
    def add_professional_branding(self, ax):
        """Add professional branding elements"""
        
        # Company/brand logo area (left side)
        logo_bg = FancyBboxPatch(
            (0.03, 0.92), 0.15, 0.06,
            boxstyle=f"round,pad={self.spacing['xs']}",
            facecolor=self.colors['corporate_blue'],
            alpha=0.9
        )
        ax.add_patch(logo_bg)
        
        # Brand text
        ax.text(0.105, 0.95, 'FITNESS PRO', 
               fontsize=10, fontweight='bold',
               color=self.colors['white'],
               ha='center', va='center',
               transform=ax.transAxes)
               
        ax.text(0.105, 0.925, 'TRAINING SYSTEM', 
               fontsize=7, fontweight='600',
               color=self.colors['white'],
               ha='center', va='center',
               transform=ax.transAxes)
               
    def create_professional_day_indicator(self, ax, day_info):
        """Create professional day indicator"""
        
        # Professional day badge
        day_bg = FancyBboxPatch(
            (0.82, 0.92), 0.15, 0.06,
            boxstyle=f"round,pad={self.spacing['xs']}",
            facecolor=self.colors['professional_teal'],
            edgecolor=self.colors['border_gray'],
            linewidth=1
        )
        ax.add_patch(day_bg)
        
        # Day information
        ax.text(0.895, 0.955, f'DAY {day_info["day_number"]}', 
               fontsize=11, fontweight='bold',
               color=self.colors['white'],
               ha='center', va='center',
               transform=ax.transAxes)
               
        ax.text(0.895, 0.93, 'of 4', 
               fontsize=8, fontweight='400',
               color=self.colors['white'],
               ha='center', va='center',
               transform=ax.transAxes, alpha=0.9)
               
    def add_professional_metadata(self, ax):
        """Add professional header metadata"""
        
        # Current date and time
        current_date = datetime.now().strftime("%B %d, %Y")
        current_time = datetime.now().strftime("%H:%M")
        
        # Professional date styling
        ax.text(0.95, 0.895, current_date,
               fontsize=self.typography['caption']['size'],
               color=self.colors['slate'],
               ha='right', va='center',
               transform=ax.transAxes)
               
        ax.text(0.95, 0.875, f'Generated at {current_time}',
               fontsize=self.typography['caption']['size'],
               color=self.colors['slate'],
               ha='right', va='center',
               transform=ax.transAxes)
               
        # Professional document info
        ax.text(0.05, 0.875, 'Professional Training Protocol',
               fontsize=self.typography['caption']['size'],
               color=self.colors['slate'],
               ha='left', va='center',
               transform=ax.transAxes, style='italic')
               
    def create_professional_table(self, ax, data, day_info):
        """Create professional business-grade table"""
        
        if not data or len(data) < 2:
            return
            
        header = data[0]
        rows = data[1:]
        
        # Table layout
        table_y_start = 0.82
        table_height = 0.55
        col_widths = [0.32, 0.14, 0.16, 0.12, 0.26]
        row_height = table_height / len(data)
        
        # Professional table container
        self.create_professional_table_container(ax, table_y_start, table_height)
        
        # Professional table header
        self.create_professional_table_header(ax, header, table_y_start, row_height, col_widths)
        
        # Professional table rows
        self.create_professional_table_rows(ax, rows, table_y_start, row_height, col_widths)
        
        # Professional enhancements
        self.add_professional_enhancements(ax, day_info, rows)
        
    def create_professional_table_container(self, ax, y_start, height):
        """Create professional table container"""
        
        # Professional shadow
        shadow = FancyBboxPatch(
            (0.05 + self.spacing['xs'], y_start - height - self.spacing['xs']), 0.9, height,
            boxstyle=f"round,pad={self.spacing['sm']}",
            facecolor=self.colors['corporate_gray'],
            alpha=0.1
        )
        ax.add_patch(shadow)
        
        # Main professional container
        container = FancyBboxPatch(
            (0.05, y_start - height), 0.9, height,
            boxstyle=f"round,pad={self.spacing['sm']}",
            facecolor=self.colors['surface_white'],
            edgecolor=self.colors['border_gray'],
            linewidth=self.borders['width_medium']
        )
        ax.add_patch(container)
        
    def create_professional_table_header(self, ax, header, y_start, row_height, col_widths):
        """Create professional table header"""
        
        header_y = y_start - row_height
        
        # Professional header background
        header_gradient = np.linspace(0, 1, 256).reshape(1, -1)
        ax.imshow(header_gradient, extent=[0.055, 0.945, header_y + 0.005, y_start - 0.005], 
                 aspect='auto', cmap=self.corporate_gradient, alpha=0.9)
                 
        # Header border
        header_border = FancyBboxPatch(
            (0.055, header_y + 0.005), 0.89, row_height - 0.01,
            boxstyle=f"round,pad={self.spacing['xs']}",
            facecolor='none',
            edgecolor=self.colors['corporate_blue'],
            linewidth=1
        )
        ax.add_patch(header_border)
        
        # Professional header content
        header_icons = ['strength', 'metrics', 'progress', 'time', 'achievement']
        x_pos = 0.06
        
        for i, (col, icon_name) in enumerate(zip(header, header_icons)):
            # Professional icon
            if icon_name in self.icons:
                self.icons[icon_name](ax, x_pos + 0.012, header_y + row_height/2, 
                                    0.01, self.colors['white'])
            
            # Header text
            ax.text(x_pos + 0.03, header_y + row_height/2, col,
                   fontsize=self.typography['header']['size'],
                   fontweight=self.typography['header']['weight'],
                   color=self.typography['header']['color'],
                   ha='left', va='center', transform=ax.transAxes)
            
            x_pos += col_widths[i]
            
    def create_professional_table_rows(self, ax, rows, y_start, row_height, col_widths):
        """Create professional table rows"""
        
        header_y = y_start - row_height
        
        for row_idx, row in enumerate(rows):
            y_pos = header_y - (row_idx + 1) * row_height
            
            # Professional row styling
            if row_idx % 2 == 0:
                row_color = self.colors['white']
            else:
                row_color = self.colors['light_gray']
                
            # Row background
            row_bg = Rectangle((0.055, y_pos + 0.001), 0.89, row_height - 0.002,
                             facecolor=row_color, alpha=0.7)
            ax.add_patch(row_bg)
            
            # Exercise classification
            exercise_type = self.classify_exercise(row[0])
            type_color = self.get_professional_exercise_color(exercise_type)
            
            # Professional type indicator
            type_indicator = Rectangle((0.05, y_pos), 0.005, row_height,
                                     facecolor=type_color, alpha=0.9)
            ax.add_patch(type_indicator)
            
            # Exercise icon
            if exercise_type in self.icons:
                self.icons[exercise_type](ax, 0.052, y_pos + row_height/2, 
                                        0.008, type_color)
            
            # Professional row data
            x_pos = 0.06
            for col_idx, cell in enumerate(row):
                # Professional text styling
                text_style = self.get_professional_text_style(col_idx)
                
                # Cell text
                ax.text(x_pos + 0.005, y_pos + row_height/2, str(cell),
                       fontsize=text_style['size'],
                       fontweight=text_style['weight'],
                       color=text_style['color'],
                       ha='left', va='center',
                       transform=ax.transAxes)
                
                x_pos += col_widths[col_idx]
                
            # Professional row border
            if row_idx < len(rows) - 1:  # Not last row
                ax.plot([0.055, 0.945], [y_pos, y_pos], 
                       color=self.colors['border_gray'], linewidth=0.5, alpha=0.5)
                       
    def add_professional_enhancements(self, ax, day_info, rows):
        """Add professional visual enhancements"""
        
        # Professional summary panel
        self.create_professional_summary_panel(ax, day_info, rows)
        
        # Professional progress indicator
        self.create_professional_progress_bar(ax, day_info)
        
        # Professional footer
        self.add_professional_footer(ax)
        
    def create_professional_summary_panel(self, ax, day_info, rows):
        """Create professional workout summary panel"""
        
        # Panel background
        panel_bg = FancyBboxPatch(
            (0.58, 0.05), 0.4, 0.15,
            boxstyle=f"round,pad={self.spacing['md']}",
            facecolor=self.colors['light_gray'],
            edgecolor=self.colors['border_gray'],
            linewidth=1
        )
        ax.add_patch(panel_bg)
        
        # Panel header
        panel_header = FancyBboxPatch(
            (0.585, 0.17), 0.39, 0.025,
            boxstyle=f"round,pad={self.spacing['xs']}",
            facecolor=self.colors['corporate_blue'],
            alpha=0.9
        )
        ax.add_patch(panel_header)
        
        ax.text(0.775, 0.1825, 'WORKOUT SUMMARY',
               fontsize=9, fontweight='bold',
               color=self.colors['white'],
               ha='center', va='center',
               transform=ax.transAxes)
        
        # Summary metrics
        metrics = self.calculate_professional_metrics(rows, day_info)
        
        metric_positions = [(0.59, 0.145), (0.59, 0.12), (0.59, 0.095), (0.59, 0.07)]
        metric_icons = ['strength', 'time', 'progress', 'achievement']
        
        for i, ((label, value), pos, icon) in enumerate(zip(metrics.items(), metric_positions, metric_icons)):
            # Icon
            if icon in self.icons:
                self.icons[icon](ax, pos[0], pos[1], 0.008, self.colors['corporate_blue'])
            
            # Label
            ax.text(pos[0] + 0.02, pos[1], f'{label}:', 
                   fontsize=self.typography['caption']['size'],
                   fontweight='500',
                   color=self.colors['charcoal'],
                   ha='left', va='center', transform=ax.transAxes)
            
            # Value
            ax.text(0.96, pos[1], str(value),
                   fontsize=self.typography['label']['size'],
                   fontweight='600',
                   color=self.colors['corporate_blue'],
                   ha='right', va='center', transform=ax.transAxes)
                   
    def create_professional_progress_bar(self, ax, day_info):
        """Create professional progress indicator"""
        
        progress = day_info['day_number'] / 4.0
        
        # Progress container
        progress_container = FancyBboxPatch(
            (0.05, 0.22), 0.9, 0.02,
            boxstyle=f"round,pad={self.spacing['xs']}",
            facecolor=self.colors['light_gray'],
            edgecolor=self.colors['border_gray'],
            linewidth=1
        )
        ax.add_patch(progress_container)
        
        # Progress fill
        if progress > 0:
            progress_fill = FancyBboxPatch(
                (0.055, 0.225), 0.89 * progress, 0.01,
                boxstyle=f"round,pad={self.spacing['xs']}",
                facecolor=self.colors['success_green'],
                alpha=0.9
            )
            ax.add_patch(progress_fill)
            
        # Progress text
        ax.text(0.5, 0.255, f'Training Program Progress: {int(progress * 100)}% Complete',
               fontsize=self.typography['caption']['size'],
               fontweight='600',
               color=self.colors['corporate_blue'],
               ha='center', va='center', transform=ax.transAxes)
               
    def add_professional_footer(self, ax):
        """Add professional document footer"""
        
        # Footer separator line
        ax.plot([0.05, 0.95], [0.025, 0.025], 
               color=self.colors['border_gray'], linewidth=1)
               
        # Footer content
        ax.text(0.05, 0.015, '© 2025 Professional Fitness Training System',
               fontsize=7, color=self.colors['slate'],
               ha='left', va='center', transform=ax.transAxes)
               
        ax.text(0.95, 0.015, 'Confidential Training Protocol',
               fontsize=7, color=self.colors['slate'],
               ha='right', va='center', transform=ax.transAxes, style='italic')
               
    def classify_exercise(self, exercise_name):
        """Classify exercise for professional categorization"""
        
        name_lower = exercise_name.lower()
        
        if any(word in name_lower for word in ['warm', 'stretch', 'cool']):
            return 'warmup'
        elif any(word in name_lower for word in ['cardio', 'run', 'bike', 'row', 'treadmill']):
            return 'cardio'
        elif any(word in name_lower for word in ['plank', 'crunch', 'twist', 'core']):
            return 'core'
        elif any(word in name_lower for word in ['press', 'curl', 'raise', 'squat', 'deadlift']):
            return 'strength'
        else:
            return 'flexibility'
            
    def get_professional_exercise_color(self, exercise_type):
        """Get professional colors for exercise types"""
        
        color_map = {
            'strength': self.colors['corporate_blue'],
            'cardio': self.colors['business_green'],
            'flexibility': self.colors['accent_purple'],
            'core': self.colors['warning_amber'],
            'warmup': self.colors['professional_teal']
        }
        return color_map.get(exercise_type, self.colors['corporate_gray'])
        
    def get_professional_text_style(self, col_idx):
        """Get professional text styling for columns"""
        
        styles = {
            0: {'size': 9, 'weight': '600', 'color': self.colors['executive_navy']},    # Exercise
            1: {'size': 9, 'weight': '600', 'color': self.colors['corporate_blue']},   # Sets/Reps
            2: {'size': 9, 'weight': '500', 'color': self.colors['business_green']},   # Load
            3: {'size': 8, 'weight': '400', 'color': self.colors['charcoal']},         # Rest
            4: {'size': 8, 'weight': '400', 'color': self.colors['slate']},            # Notes
        }
        return styles.get(col_idx, {'size': 8, 'weight': '400', 'color': self.colors['charcoal']})
        
    def calculate_professional_metrics(self, rows, day_info):
        """Calculate professional workout metrics"""
        
        main_exercises = [r for r in rows if not self.is_warmup_cooldown(r[0])]
        
        return {
            'Total Exercises': len(main_exercises),
            'Estimated Duration': f'{len(main_exercises) * 3 + 15} minutes',
            'Training Intensity': f'Level {day_info["day_number"]}',
            'Caloric Expenditure': f'~{320 + day_info["day_number"] * 40} kcal'
        }
        
    def is_warmup_cooldown(self, exercise_name):
        """Check if exercise is warmup or cooldown"""
        name_lower = exercise_name.lower()
        return any(word in name_lower for word in ['warm', 'stretch', 'cool'])

def create_professional_graphics_fitness_plan():
    """Create professional graphics fitness plan"""
    
    # Professional workout data
    workout_days = {
        'Day 1 – Upper Body Strength Development': {
            'day_number': 1,
            'focus': 'Upper Body Push Pattern + Cardiovascular Training',
            'data': [
                ['Exercise Name', 'Sets × Reps', 'Training Load', 'Rest Period', 'Technical Notes'],
                ['Dynamic Movement Preparation', '1 × 10 minutes', 'Bodyweight Protocol', 'N/A', 'Focus on mobility and activation'],
                ['Cardiovascular Training (Treadmill)', '30 minutes', 'Moderate Intensity', 'N/A', 'Alternative: Elliptical for joint comfort'],
                ['Incline Dumbbell Bench Press', '3 × 10-12', '10-12 kg per hand', '60-90 sec', 'Maintain scapular stability'],
                ['Standing Overhead Press', '3 × 12', '20 kg barbell', '60-90 sec', 'Engage core throughout movement'],
                ['Lateral Shoulder Raise', '2 × 15', '4-6 kg dumbbells', '30-45 sec', 'Control eccentric phase'],
                ['Triceps Cable Extension', '3 × 12-15', 'Moderate resistance', '45-60 sec', 'Keep elbows stationary'],
                ['Active Recovery Walk', '10 minutes', '5-7% incline', 'N/A', 'Maintain natural gait pattern']
            ]
        },
        'Day 2 – Lower Body Power Development': {
            'day_number': 2,
            'focus': 'Quadriceps Emphasis + Cardiovascular Conditioning',
            'data': [
                ['Exercise Name', 'Sets × Reps', 'Training Load', 'Rest Period', 'Technical Notes'],
                ['Dynamic Lower Body Preparation', '1 × 10 minutes', 'Movement-based', 'N/A', 'Hip and ankle mobility focus'],
                ['Stationary Bike Training', '20-30 minutes', '90 RPM target', 'N/A', 'Low-impact cardiovascular option'],
                ['Leg Press Machine', '3 × 12', 'Progressive loading', '60-90 sec', 'Range of motion to 90 degrees'],
                ['Goblet Squat', '3 × 10-12', '10-20 kg dumbbell', '60 sec', 'Descend to parallel position'],
                ['Step-Up Exercise', '2 × 12 each leg', 'Bodyweight + 5-10 kg', '45-60 sec', 'Drive through heel'],
                ['Prone Hamstring Curl', '3 × 15', 'Light-moderate load', '45-60 sec', 'Controlled movement pattern'],
                ['Standing Calf Raise', '3 × 15', 'Bodyweight progression', '30-45 sec', 'Full range of motion'],
                ['Plank Hold', '3 × 30-45 seconds', 'Isometric hold', '30 sec', 'Maintain neutral spine'],
                ['Flexibility Cool-Down', '5-10 minutes', 'Static stretching', 'N/A', 'Focus on worked muscle groups']
            ]
        },
        'Day 3 – Upper Body Pull Development': {
            'day_number': 3,
            'focus': 'Posterior Chain + Cardiovascular Enhancement',
            'data': [
                ['Exercise Name', 'Sets × Reps', 'Training Load', 'Rest Period', 'Technical Notes'],
                ['Upper Body Movement Prep', '1 × 8-10 minutes', 'Dynamic preparation', 'N/A', 'Shoulder and thoracic mobility'],
                ['Rowing Machine Intervals', '20 minutes', 'Moderate intensity', 'N/A', '1:1 work-to-rest ratio'],
                ['Assisted Pull-Up', '3 × 8-10', 'Appropriate assistance', '90 sec', 'Full range of motion'],
                ['Seated Cable Row', '3 × 12', 'Moderate resistance', '60-90 sec', 'Retract shoulder blades'],
                ['Cable Face Pull', '2 × 15', 'Light resistance', '45 sec', 'High elbow position'],
                ['Barbell Biceps Curl', '3 × 10', '20-25 kg barbell', '60 sec', 'Avoid momentum'],
                ['Side Plank', '2 × 30 sec each side', 'Bodyweight', '30 sec', 'Maintain hip alignment'],
                ['Recovery Stretching', '5-10 minutes', 'Static holds', 'N/A', 'Upper body focus']
            ]
        },
        'Day 4 – Posterior Chain Development': {
            'day_number': 4,
            'focus': 'Glutes & Hamstrings + Functional Conditioning',
            'data': [
                ['Exercise Name', 'Sets × Reps/Duration', 'Training Load', 'Rest Period', 'Technical Notes'],
                ['Dynamic Hip Preparation', '1 × 10 minutes', 'Movement-based', 'N/A', 'Hip mobility and glute activation'],
                ['Incline Treadmill Walk', '15 minutes', '8-15% gradient', 'N/A', 'Optional weighted vest'],
                ['Romanian Deadlift', '3 × 10', '40 kg barbell', '90 sec', 'Hip hinge movement pattern'],
                ['Glute Bridge', '3 × 15', 'Bodyweight + 10-20 kg', '60 sec', 'Squeeze glutes at top'],
                ['Walking Lunge', '2 × 10 each leg', 'Bodyweight + 5 kg', '60 sec', 'Control descent phase'],
                ['Single-Leg Hamstring Curl', '2 × 10 each leg', 'Bodyweight', '45 sec', 'Maintain core stability'],
                ['Farmer\'s Walk', '3 × 30 seconds', 'Heavy implements', '60 sec', 'Upright posture'],
                ['Recovery Walk', '5-10 minutes', 'Level surface', 'N/A', 'Gentle pace for recovery']
            ]
        }
    }
    
    # Create professional tracker
    tracker = ProfessionalGraphicsFitnessTracker()
    pdf_path = 'Professional_Graphics_Fitness_Tracker.pdf'
    
    with PdfPages(pdf_path) as pdf:
        for day_title, day_info in workout_days.items():
            # Professional high-resolution figure
            fig, ax = plt.subplots(figsize=(11.69, 8.27), dpi=300)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            fig.patch.set_facecolor('white')
            
            # Create professional header
            tracker.create_professional_header(ax, day_title,
                                             subtitle=f"Professional Training Protocol - {day_info['focus']}",
                                             day_info=day_info)
            
            # Create professional table
            tracker.create_professional_table(ax, day_info['data'], day_info)
            
            # Save with professional quality
            pdf.savefig(fig, bbox_inches='tight', dpi=300, 
                       facecolor='white', edgecolor='none')
            plt.close(fig)
    
    return pdf_path

if __name__ == "__main__":
    print("🏢 CREATING PROFESSIONAL GRAPHICS FITNESS TRACKER 🏢")
    print("📊 Applying corporate design standards...")
    print("💼 Implementing business-grade aesthetics...")
    print("📋 Adding professional visual elements...")
    print("🎯 Optimizing for executive presentation...")
    print("📈 Integrating advanced graphics system...")
    
    pdf_path = create_professional_graphics_fitness_plan()
    
    print(f"\n🎉 PROFESSIONAL GRAPHICS FITNESS TRACKER COMPLETED! 🎉")
    print(f"📄 File: {pdf_path}")
    print(f"📍 Location: {os.path.abspath(pdf_path)}")
    print(f"\n💼 PROFESSIONAL FEATURES:")
    print("✅ Corporate-grade color palette")
    print("✅ Business-standard typography")
    print("✅ Professional visual hierarchy")
    print("✅ Executive-level presentation")
    print("✅ Clean, modern design aesthetics")
    print("✅ Professional icons and graphics")
    print("✅ Sophisticated layout structure")
    print("✅ Corporate branding elements")
    print("✅ High-quality visual components")
    print("✅ Business-ready documentation")
    print("✅ Professional summary panels")
    print("✅ Corporate progress indicators")
    print("✅ Executive metadata display")
    print("✅ Professional footer information")
    print("✅ Clean graphics integration")
    print(f"\nYour fitness tracker is now PROFESSIONAL + GRAPHICS! 🏆")
