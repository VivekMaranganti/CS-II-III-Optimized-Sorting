import Swift
import Foundation


let characterset = CharacterSet(charactersIn:"abcdefghijklmnopqrstuvwxyz")

func wordsort(arrl: [String]) -> [String]{
    var newarr = [String]()
    var arr = arrl
    while !arr.isEmpty{
        var lowNum = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        var lowdex = 0
        for i in 0..<arr.count{
            if (arr[i]<lowNum){
                lowNum=arr[i]
                lowdex=i
            }
        }
        newarr.append(arr.remove(at: lowdex))
    }
    return newarr
}


func removespecial(_ unsortedl: [String]) -> (Dictionary<String,String>, [String]){
    var dic = [String: String]()
    var unsorted = unsortedl  
    for i in 0..<unsorted.count{
        let word = unsorted[i]
        if word.rangeOfCharacter(from: characterset.inverted) != nil {
            let newword = word.filter("abcdefghijklmnopqrstuvwxyz".contains)
            dic[newword] = word
            unsorted[i] = newword
        }
    }
    return (dic,unsorted)
}



func returnspecial(sortedl: [String], dic: Dictionary<String,String> ) -> [String]{
    var sorted = sortedl
    for i in 0..<sorted.count{
        if let _ = dic[sorted[i]]{
            sorted[i] = dic[sorted[i]]!
        }
    }
    return sorted
}

var unsortedList = [String]()
while let line = readLine() {
    unsortedList.append(line.replacingOccurrences(of: "\n", with: "").lowercased())
}
var yo = removespecial(unsortedList)
var dic = yo.0
unsortedList = yo.1
var sortedList = wordsort(arrl: unsortedList)
sortedList = returnspecial(sortedl: sortedList, dic: dic)

for word in sortedList{
    print(word)
}
