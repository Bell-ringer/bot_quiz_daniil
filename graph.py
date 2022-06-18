import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


async def graph(c1, c2, c3, c4, c5, c6, c7, c8, user_id):
    # Each attribute we'll plot in the radar chart.
    labels = ['Способность использовать современные методы и технологии обучения',
              'Способность решать задачи воспитания',
              'Диагностика',
              'Способность осуществлять обучение с учётом социальных,\n возрастных, психофизических и индивидуальных особенностей',
              'Цифровая грамотность',
              'Готовность к охране и безопасности',
              'Коммуникация',
              'Готовность к профессиональной деятельности']

    values = [c1, c2, c3, c4, c5, c6, c7, c8]

    # Number of variables we're plotting.
    num_vars = len(labels)

    # Split the circle into even parts and save the angles
    # so we know where to put each axis.
    angles = list(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))

    # The plot is a circle, so we need to "complete the loop"
    # and append the start value to the end.
    # angles += angles[0]
    # values += values[0]

    # ax = plt.subplot(polar=True)
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Draw the outline of our data.
    ax.plot(angles, values, color='#1aaf6c', linewidth=1)
    # Fill it in.
    ax.fill(angles, values, color='#1aaf6c', alpha=0.25)

    # Fix axis to go in the right order and start at 12 o'clock.
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Draw axis lines for each angle and label.
    ax.set_thetagrids(np.degrees(angles), labels)

    # Go through labels and adjust alignment based on where
    # it is in the circle.
    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')

    # Ensure radar goes from 0 to 100.
    ax.set_ylim(0, 100)
    # You can also set gridlines manually like this:
    # ax.set_rgrids([20, 40, 60, 80, 100])

    # Set position of y-labels (0-100) to be in the middle
    # of the first two axes.
    ax.set_rlabel_position(180 / num_vars)

    # Add some custom styling.
    # Change the color of the tick labels.
    ax.tick_params(colors='#222222')
    # Make the y-axis (0-100) labels smaller.
    ax.tick_params(axis='y', labelsize=8)
    # Change the color of the circular gridlines.
    ax.grid(color='#AAAAAA')
    # Change the color of the outermost gridline (the spine).
    ax.spines['polar'].set_color('#222222')
    # Change the background color inside the circle itself.
    ax.set_facecolor('#FAFAFA')

    # Lastly, give the chart a title and give it some
    # padding above the "Acceleration" label.
    ax.set_title('Результаты теста', y=1.08)

    filename = "results_" + str(user_id) + ".png"

    plt.savefig(filename, bbox_inches='tight')
