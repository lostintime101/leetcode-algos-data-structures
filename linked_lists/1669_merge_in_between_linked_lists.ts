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

function mergeInBetween(list1: ListNode | null, a: number, b: number, list2: ListNode | null): ListNode | null {

    let head = list1;

    for(let i=0; i<a-1; i++){
        head = head.next;
    };

    let final_section = head.next;

    for(let i=0; i<(b-a)+1; i++){
        final_section = final_section.next;
    };

    head.next = list2;

    while(head.next != null){
        head = head.next;
    };

    head.next = final_section;

    return list1;

};