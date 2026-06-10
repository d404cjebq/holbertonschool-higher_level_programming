#!/usr/bin/python3
"""
هذا الموديول يحتوي على دالة لجمع عددين صحيحين.
يوفر الدالة add_integer التي تقبل أعداداً صحيحة أو عشرية وتجمعها.
"""


def add_integer(a, b=98):
    """تضيف عددين صحيحين بعد تحويلهما (إذا كانا عشريين).

    Args:
        a: العدد الأول (int أو float).
        b: العدد الثاني (int أو float)، القيمة الافتراضية هي 98.

    Raises:
        TypeError: إذا لم يكن a أو b عدداً صحيحاً أو عشرياً.

    Returns:
        القيمة الناتجة عن جمع a و b كعدد صحيح.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
