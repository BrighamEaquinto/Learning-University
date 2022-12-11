using DataFrames, Chain

df = DataFrame(group = [1, 2, 1, 2], weight = [1, 3, 5, 7])

result = @chain df begin
    filter(r -> r.weight < 6, _)
    groupby(:group)
    combine(:weight => sum => :total_weight)
end