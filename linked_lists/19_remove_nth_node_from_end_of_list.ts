/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {

    let N = 0;
    let curr = head;

    while(curr !== null){
        N ++;
        curr = curr.next;
    }

    N -= n;
    if(N === 0){
        head = head.next;
    }

    let count = 0;
    curr = head;

    console.log(curr, N, count);
    while(curr !== null){
        count ++;
        if(count === N){
            curr.next = curr.next.next;
        }
        curr = curr.next;
    }

    return head;
};