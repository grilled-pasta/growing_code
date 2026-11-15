# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alla <alkonsta@student.codam.nl>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/15 09:56:43 by alla              #+#    #+#              #
#    Updated: 2026/11/15 09:57:37 by alla             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
    x = int(input("Enter length: "))
    y = int(input("Enter width: "))
    print(f"Plot area: {x * y}")
