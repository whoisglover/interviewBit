  
'''
prototype questions to memorize:
linked-lists:
    - reverse a linked list: multiple pointers to keep track
    - identify a cycle in a linked list: fast runner, slow resultContainer
hashMap:
    - get comfortable with storing and getting data
'''``

'''
Example question: Least recently used cache

LinkedHashMap

'''

class LRUCache extends LinkedHashMap<K,V>{

    LRUCache(int capacity) {
        super(capacity)
    }
}


// capacity?
// usage?
// speed constraints?
// device constraints?

//requirements:
// fast writes
// fast reads
// identify iteems in cache
// knowing order of insertion in cache
// fast removals

class Data {

}

class Node {
  String key;
  Data value;
  public Node next;
  public Node prev;

  Node(String key, Data value){
    this.key = key;
    this.value = value;
  }
}

capacity = 3

Head {key: "wwww.google.com"
      value: "abcd"
      next: null
      prev: null,
}

Tail {
  key: "www.yahoo.com"
  value: "ffff"

}

{
  "www.google.com": "abcd",
  "www.facebook.com": "dbca",
  "www.yahoo.com": "fffff"

}



class LRUCache {
  HashMap<String, Data> dataMap;
  Node head;
  Node tail;

  LRUCache(int capacity){
    this.capacity = capacity;
    dataMap = new HashMap<>();
  }

  public void put(String key, Data value){
    Node node;
    if(!dataMap.containsKey(key)){
      node = new Node(key, value);
      if(shouldRemoveEldest){
        dataMap.remove(tail.key)
        tail.prev.next = null
        tail = tail.prev
      }
      dataMap.put(key,value);
      setHead(node);
    } else {
      node = dataMap.get(key);
      remove(node);
      set(node);
    }
  }



  public Data get(String key) {
    if(dataMap.containsKey(key)){
      node = dataMap.get(key);
      remove(node);
      set(node);
      return dataMap.get(key).value;
    } else {
      return null;
    }
  }

  private boolean shouldRemoveEldest() {
    return dataMap.size() >= capacity;
  }

  private void setHead(Node node) {
    if(node != null) {
      node.next = head
      if(head != null) {
        head.prev = node
      }
      head = node
    }
    if(tail == null){
      tail = node
    }
  }


  public void remove(Node node){
    //TODO: handle removal of nodes at the beginning and nodes at the end
    if(node != null){
      if(node.prev != null){
        node.prev.next = node.next
        node.prev = null
      } else {
        head = node.next
      }
      if(node.next != null){
        node.next.prev = node.prev
        node.next = null
      }
    }
  }
}
