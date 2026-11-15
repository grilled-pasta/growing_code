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

def ft_count_harvest_recursive() -> None:
    def countdown(n: int) -> None:
        if n > 1:
            countdown(n - 1)
        print(f"Day {n}")
    days = int(input("Days until harvest: "))
    countdown(days)
    print("Harvest time!")
