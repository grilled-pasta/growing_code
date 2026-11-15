#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/15 20:01:34 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/15 20:01:34 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    x = int(input("Enter length: "))
    y = int(input("Enter width: "))
    print(f"Plot area: {x * y}")
