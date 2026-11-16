#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/15 20:11:59 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/15 20:11:59 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

# DEFAULT PARAMETER VALUES + if case
def ft_count_harvest_recursive(days: int | None = None) -> None:
    if days is None:
        days = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days)
        print("Harvest time!")
    elif days > 0:
        if days > 1:
            ft_count_harvest_recursive(days - 1)
        print(f"Day {days}")

# NESTED RECURSIVE FUNCTION
# def ft_count_harvest_recursive() -> None:
#     def countdown(n: int) -> None:
#         if n > 1:
#             countdown(n - 1)
#         print(f"Day {n}")
#     days = int(input("Days until harvest: "))
#     if days > 0:
#       countdown(days)
#     print("Harvest time!")
#

# HELPER RECURSIVE FUNCTION
# def ft_count_harvest_recursive() -> None:
#     days = int(input("Days until harvest: "))
#     if days > 0:
#         countdown(days)
#     print("Harvest time!")
#
#
# def countdown(n: int) -> None:
#     if n > 1:
#         countdown(n - 1)
#     print(f"Day {n}")

# DEFAULT PARAMETER VALUES + match case
# def ft_count_harvest_recursive(days: int | None = None) -> None:
#     match days:
#         case None:
#             days = int(input("Days until harvest: "))
#             ft_count_harvest_recursive(days)
#             print("Harvest time!")
#         case int() as n if n > 0:
#             match n:
#                 case int() if n > 1:
#                     ft_count_harvest_recursive(days - 1)
#                 case _:
#                     pass
#             print(f"Day {days}")
#         case _:
#             pass
