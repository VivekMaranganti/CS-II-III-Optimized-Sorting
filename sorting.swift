import Swift
import Foundation

let alpDict: Dictionary<Int, Character>
let alpDict2: Dictionary<Character, Int>
alpDict = [ 0:" ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"]
alpDict2 = [ " ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26]
let characterset = CharacterSet(charactersIn:"abcdefghijklmnopqrstuvwxyz")


func wordtonum(w: String) -> Float80{
    let n = w.count
    var num = Float80(0)
    for i in 0..<n{
        let digit = Float80(alpDict2[w[w.index(w.startIndex, offsetBy: i)]]!)
        num = num + digit*Float80(pow(27.0,Double(n-i-1)))
    }
    return num

}

func numtoword(numl: Float80) -> String{
    var word = ""
    var num: UInt64
    if numl > Float80(UInt64.max){
        num = UInt64.max
    }else{
        num = UInt64(numl)
    }
    if num==0{
        return ""
    }
    while num>0 {
        let mod = num % 27
        num = UInt64(floor(Double(num) / 27))
        word = String(alpDict[Int(mod)]!) + word
    }
    return word
}


func wordsort(arrl: [String]) -> [String]{
    var arr = arrl
    var maxlen = 0
    for word in arr{
        if (word.count>maxlen){ maxlen = word.count}
    }
    for i in 0..<arr.count{
        let ros = String(repeating:" ", count: maxlen-arr[i].count)
        arr[i] += ros
    }
    var numlist = arr.map{wordtonum(w: $0)}
    numlist = numsort(arrl: numlist)
    let sortedarray = numlist.map{numtoword(numl: $0).replacingOccurrences(of: " ", with: "")}
    return sortedarray
}



func numsort(arrl: [Float80]) -> [Float80]{
    var newarr = [Float80]()
    var arr = arrl
    while !arr.isEmpty{
        var lowNum = Float80(pow(2.0,79)-1)
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
