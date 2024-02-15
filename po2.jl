# PROBLEM 1
# DATA
D = 260*12 # Year demand (260 units/month)
c = 3 # Unit cost ($)
h = 0.25 # Holding rate
ce = h*c # Holding cost
ct = 20 # Ordering cost

# OPTIMAL POLICY
Q_opt = sqrt(2*D*ct/ce) # EOQ
TRC_optimal = sqrt(2*D*ct*ce) # Minimum TRC
T_opt = Q_opt/D # Reorder interval (years)
T_opt_months = T_opt*12 # Reorder interval (months)
N = D/Q_opt # Orders per year

begin # PLOT OPTIMAL POLICY
    using GLMakie
    GLMakie.activate!(inline=true)
    fig = Figure(size=(750,250))
    set_theme!(Theme(fontsize=18))
    
    ax1 = Axis(fig[1, 1], limits=(0,12, 0,600), title = "Optimal Policy (T = 1.57 months)")
    ax1.xticks = 0:1:12

    interval_1 = 12/(N)
    x1 = [T for T in 0:interval_1:52 for _ in 1:2][begin:end-1]
    y1 = [iseven(i) ? Q_opt : 0 for i in 1:length(x1)]
    lines!(ax1, x1, y1)
    fig
end

# POWERS-OF-2 POLICY
T_opt_months/sqrt(2) # Lower bound
T_opt_months*sqrt(2) # Upper bound
T_po2 = 2/12 # Po2 reorder interval (years)
Q_po2 = D*T_po2 # Po2 order quantity
N_po2 = D/Q_po2 # Po2 orders per year

begin # PLOT POWERS-OF-TWO POLICY
    fig = Figure(size=(750,500))
    set_theme!(Theme(fontsize=18))
    ax1 = Axis(fig[1, 1], limits=(0,12, 0,600), title = "Optimal Policy (T = 1.57 months)")
    ax1.xticks = 0:1:12
    ax2 = Axis(fig[2, 1], limits=(0,12, 0,600), title = "Powers-of-Two (T = 2 months)")
    ax2.xticks = 0:1:12

    lines!(ax1, x1, y1) # Previous plot
    interval_2 = 12/(N_po2)
    x2 = [T for T in 0:interval_2:12+interval_2 for _ in 1:2][begin:end-1]
    y2 = [iseven(i) ? Q_po2 : 0 for i in 1:length(x2)]
    lines!(ax2, x2, y2)
    fig
end

# COST SENSITIVITY: CHANGES IN THE TRC
TRC_optimal
TRC_po2 = ct*(D/Q_po2) + ce*(Q_po2/2)
TRC_po2/TRC_optimal

(1/2)*(T_po2/T_opt + T_opt/T_po2)














# PROBLEM 2
# DATA
D_1 = 2000 # Year Demand
D_2 = 1500
c_1 = 200 # Unit cost
c_2 = 150
h = 0.25 # Holding rate
ce_1 = h*c_1 # Holding cost 1
ce_2 = h*c_2 # Holding cost 2
ct_purchase = 80 # Purchase Cost
ct_trucking = 500 # Trucking Cost
ct = ct_purchase + ct_trucking # Ordering Cost

# OPTIMAL POLICIES
# PRODUCT 1
Q_opt_1 = sqrt(2*D_1*ct/(ce_1)) # EOQ
N_1 = D_1/Q_opt_1 # Number of orders per year
TRC_opt_1 = sqrt(2*D_1*ct*ce_1)
T_opt_1 = Q_opt_1/D_1
T_opt_1_week = T_opt_1*365/7

# PRODUCT 2
Q_opt_2 = sqrt(2*D_2*ct/(ce_2))
N_2 = D_2/Q_opt_2
TRC_opt_2 = sqrt(2*D_2*ct*ce_2)
T_opt_2 = Q_opt_2/D_2
T_opt_2_week = T_opt_2*(365/7)

total_weeks = 365/7

begin # Plot Policy
    fig = Figure(size=(750,500))
    set_theme!(Theme(fontsize=20))
    ax1 = Axis(fig[1, 1], limits=(0,52, 0,300))
    ax1.xticks = 0:4:52
    ax2 = Axis(fig[2, 1], limits=(0,52, 0,300))
    ax2.xticks = 0:4:52

    interval_1 = total_weeks/N_1
    x1 = [T for T in 0:interval_1:total_weeks+interval_1 for _ in 1:2][begin:end-1]
    y1 = [iseven(i) ? Q_opt_1 : 0 for i in 1:length(x1)]
    lines!(ax1, x1, y1)
    interval_2 = total_weeks/N_2
    x2 = [Q for Q in 0:total_weeks/N_2:total_weeks+interval_2 for _ in 1:2][begin:end-1]
    y2 = [iseven(i) ? Q_opt_2 : 0 for i in 1:length(x2)]
    lines!(ax2, x2, y2)
    fig
end

# POWERS-OF-2 POLICIES
T_opt_1_week/sqrt(2) # Lower bound
T_opt_1_week*2 # Upper bound
T_po2_1 = 4
Q_po2_1 = D_1*(T_po2_1*7/365)

T_opt_2_week/sqrt(2) # Lower bound
T_opt_2_week*2 # Upper bound
T_po2_2 = 8
Q_po2_2 = D_2*(T_po2_2*7/365)

begin # Plot Policy
    fig = Figure(size=(750,500))
    set_theme!(Theme(fontsize=20))
    ax1 = Axis(fig[1, 1], limits=(0,52, 0,300))
    ax1.xticks = 0:4:52
    ax2 = Axis(fig[2, 1], limits=(0,52, 0,300))
    ax2.xticks = 0:4:52

    x1 = [T for T in 0:4:365/7+4 for _ in 1:2][begin:end-1]
    y1 = [iseven(i) ? Q_po2_1 : 0 for i in 1:length(x1)]
    lines!(ax1, x1, y1)

    x2 = [Q for Q in 0:8:365/7+4 for _ in 1:2][begin:end-1]
    y2 = [iseven(i) ? Q_po2_2 : 0 for i in 1:length(x2)]
    lines!(ax2, x2, y2)
    fig
end

# COST COMPARISON
po2_holding_1 = ce_1*Q_po2_1/2
po2_purchase_1 = ct_purchase*(D_1/Q_po2_1)
po2_trucking_1 = ct_trucking*(D_1/Q_po2_1)
po2_total_1 =  po2_holding_1 + po2_purchase_1 + po2_trucking_1

po2_holding_2 = ce_2*Q_po2_2/2
po2_purchase_2 = ct_purchase*(D_2/Q_po2_2)
po2_total_2 =  po2_holding_2 + po2_purchase_2
+
(po2_total_1 + po2_total_2) / (TRC_opt_1 +  TRC_opt_2)

# SAME REORDER INTERVALS FOR BOTH PRODUCTS

begin # Plot Policy
    fig = Figure(size=(750,500))
    set_theme!(Theme(fontsize=20))
    ax1 = Axis(fig[1, 1], limits=(0,52, 0,300))
    ax1.xticks = 0:4:52
    ax2 = Axis(fig[2, 1], limits=(0,52, 0,300))
    ax2.xticks = 0:4:52

    x1 = [T for T in 0:4:365/7+4 for _ in 1:2][begin:end-1]
    y1 = [iseven(i) ? Q_po2_1 : 0 for i in 1:length(x1)]
    lines!(ax1, x1, y1)
    x2 = [Q for Q in 0:4:365/7+4 for _ in 1:2][begin:end-1]
    y2 = [iseven(i) ? fourweek_Q_2 : 0 for i in 1:length(x2)]
    lines!(ax2, x2, y2)
    fig
end

fourweek_Q_2 = D_2*(T_po2_1*7/365) # Using Po2 interval from Product 1
fourweek_holding_2 = ce_2*fourweek_Q_2/2
fourweek_purchase_2 = ct_purchase*D_2/fourweek_Q_2
fourweek_total_2 = fourweek_holding_2 + fourweek_purchase_2

(po2_total_1 + fourweek_total_2) / (TRC_opt_1 +  TRC_opt_2)

