function plot_power_diagram(pd)
gca
hold on
for i = 1:length(pd.cell)
    pi = pd.dual_point_extended(pd.cell{i},:);
%     plot3(pi(:,1),pi(:,2),-ones(size(pi(:,1))),'r-')
    plot(pi(:,1),pi(:,2),'b-')
end
% plot(pd.point(:,1),pd.point(:,2),'r.')
box = [min(pd.point(:,1)),max(pd.point(:,1)),min(pd.point(:,2)),max(pd.point(:,2))];
axis equal
axis(box)