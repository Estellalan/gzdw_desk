function mpc = reliability_6nodes_test_system
 data_yinshan;
%% branch支路数据
mpc.branch_num =length(branch_data(:,1));    %支路数量
%branch数据说明：
%1-元件编号，2-首端节点，3-末端节点，R，X 4-故障率(次/年)，5-修复时间(h)，6-开关切换时间(h)
mpc.branch(:,1) =1:mpc.branch_num;
mpc.branch(:,2:5)=branch_data;
% [
% 1   1   2  0.3660	0.1864 0.5   1.0   0.15;
% 2   1   5  0.3811	0.1941 0.3   1.5   0.20;
% 3   2   3  0.3190	0.2070 0.2   2.0   0.50;
% 4   2   4  0.1872	0.6188 0.1   4.0   0.25;
% 5   5   6  0.4114	0.2351 0.4   3.0   0.60;];

%% node节点数据
mpc.node_num = node_num;      % 节点数量
mpc.N_B = 1;           % 负荷等级数目
for ii=1:node_num
mpc.miu_b(ii,1) = 10*randi([2, 8]);%,10*[4,3,5,1,2];     
end % 各个负荷等级价值系数
mpc.d_b = 8760;        % 各个负荷等级的持续时间
%node数据说明：1-负荷点编号，2-峰值有功负荷/MW，3-用户数，4-连接节点
mpc.node = [
1   0   0   1;
2   1   1   2;
3   1   1   3;
4   1   1   4;
5   1   1   5;
6   1   1   6;];

mpc.Pload=hourly_loads(:,:,1);
% 0.08*1000*[0.0004666666667,0.0005,0.0005666666667,0.0006333333333,0.0006666666667,0.0007333333333,0.0007666666667,0.0008,0.0008666666667,0.0009333333333,0.0009666666667,0.001,0.0009333333333,0.0008666666667,0.0008,0.0007,0.0006666666667,0.0007333333333,0.0008,0.0009333333333,0.0008666666667,0.0007333333333,0.0006,0.0005333333333;
%             0.00042,0.00045,0.00051,0.00057,0.0006,0.00066,0.00069,0.00072,0.00078,0.00084,0.00087,0.0009,0.00084,0.00078,0.00072,0.00063,0.0006,0.00066,0.00072,0.00084,0.00078,0.00066,0.00054,0.00048;
%             0.00056,0.0006,0.00068,0.00076,0.0008,0.00088,0.00092,0.00096,0.00104,0.00112,0.00116,0.0012,0.00112,0.00104,0.00096,0.00084,0.0008,0.00088,0.00096,0.00112,0.00104,0.00088,0.00072,0.00064;
%              0.00028,0.0003,0.00034,0.00038,0.0004,0.00044,0.00046,0.00048,0.00052,0.00056,0.00058,0.0006,0.00056,0.00052,0.00048,0.00042,0.0004,0.00044,0.00048,0.00056,0.00052,0.00044,0.00036,0.00032;
%             0.0002333333333,0.0001,0.0001133333333,0.0001266666667,0.0001333333333,0.0001466666667,0.0001533333333,0.00016,0.0001733333333,0.0001866666667,0.0001933333333,0.0002,0.0001866666667,0.0001733333333,0.00016,0.00014,0.0001333333333,0.0001466666667,0.00016,0.0001866666667,0.0001733333333,0.0001466666667,0.00012,0.0001066666667;
%         ];
 mpc.Qload=hourly_loads(:,:,2)
%0.05*1000*[0.00028,0.0003,0.00034,0.00038,0.0004,0.00044,0.00046,0.00048,0.00052,0.00056,0.00058,0.0006,0.00056,0.00052,0.00048,0.00042,0.0004,0.00044,0.00048,0.00056,0.00052,0.00044,0.00036,0.00032;
%             0.0001866666667,0.0002,0.0002266666667,0.0002533333333,0.0002666666667,0.0002933333333,0.0003066666667,0.00032,0.0003466666667,0.0003733333333,0.0003866666667,0.0004,0.0003733333333,0.0003466666667,0.00032,0.00028,0.0002666666667,0.0002933333333,0.00032,0.0003733333333,0.0003466666667,0.0002933333333,0.00024,0.0002133333333;
%             0.0003733333333,0.0004,0.0004533333333,0.0005066666667,0.0005333333333,0.0005866666667,0.0006133333333,0.00064,0.0006933333333,0.0007466666667,0.0007733333333,0.0008,0.0007466666667,0.0006933333333,0.00064,0.00056,0.0005333333333,0.0005866666667,0.00064,0.0007466666667,0.0006933333333,0.0005866666667,0.00048,0.0004266666667;
%             0.00014,0.00015,0.00017,0.00019,0.0002,0.00022,0.00023,0.00024,0.00026,0.00028,0.00029,0.0003,0.00028,0.00026,0.00024,0.00021,0.0002,0.00022,0.00024,0.00028,0.00026,0.00022,0.00018,0.00016;
%                    0.0004666666667,0.0005,0.0005666666667,0.0006333333333,0.0006666666667,0.0007333333333,0.0007666666667,0.0008,0.0008666666667,0.0009333333333,0.0009666666667,0.001,0.0009333333333,0.0008666666667,0.0008,0.0007,0.0006666666667,0.0007333333333,0.0008,0.0009333333333,0.0008666666667,0.0007333333333,0.0006,0.0005333333333;
% ];
% mpc.aa=[1,0.9,1.2,0.6,0.6];
% for i=1:5
%     mpc.Pload(i,:)=mpc.aa(i)*mpc.Pload(i,:);
%     mpc.Qload(i,:)=mpc.aa(i).*mpc.Qload(i,:);
% end
% mpc.Pload(5,:)=2*mpc.Pload(i,:);
% mpc.Qload(5,:)=2*mpc.Qload(i,:);
 %% power电源节点数据
mpc.power_num = 1;                     % 电源节点数量
mpc.power = 1;                         % 电源节点集合
mpc.Plimits=sum(max_loads(:,1))*0.8;
mpc.PV_cap=PV_capacities;
mpc.WT_cap=WT_capacities;
mpc.PG_cap=PG_capacities;
end