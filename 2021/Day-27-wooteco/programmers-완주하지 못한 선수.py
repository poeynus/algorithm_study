def solution(participant, completion):

    participant.sort()
    completion.sort()

    for a, b in zip(participant, completion):
        if a != b:
            return(a)
    return participant.pop()

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])

# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"