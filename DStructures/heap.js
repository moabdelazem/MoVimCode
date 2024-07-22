class Heap {
  constructor() {
    this.dataList = [];
    this.size = 0;
  }

  // Insert New Node Into The Heap
  insertNode(data) {
    let i = this.size;
    this.dataList[i] = data;
    this.size++;

    let parentIdx = Math.floor((i - 1) / 2);

    while (i != 0 && this.dataList[i] < this.dataList[parentIdx]) {
      this.dataList[i] = this.dataList[parentIdx];
      this.dataList[parentIdx] = data;
      i = parentIdx;

      parentIdx = Math.floor((i - 1) / 2);
    }
  }

  // Print The Heap Method
  printList() {
    let print_data = "";
    for (let i = 0; i < this.size; ++i) {
      print_data += this.dataList[i] + " - ";
    }
    console.log(print_data);
  }

  // Get The Size Of The Heap
  getSize() {
    return this.size;
  }
}

let heap = new Heap();

heap.insertNode(5);
heap.insertNode(3);
heap.insertNode(8);
heap.insertNode(1);
heap.insertNode(2);
heap.insertNode(10);

heap.printList();
