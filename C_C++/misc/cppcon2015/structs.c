#include <stdio.h>
#include <time.h>
#include <string.h>

struct student
{
    unsigned id;
    char *name;
    struct tm dob;
 };

 static void
 dump_student(struct student *st)
 {
    const char *dob = asctime(&st->dob);
    printf("id: %u\nname: %s\ndob: (%p) %s\n",
        st->id, st->name, dob, dob);
 }

 int
 main(void)
 {
    struct student st = {
        .id = 123,
        .name = strdup("Jon Doe"),
        .dob = {
            .tm_year = 100,
            .tm_mon = 9,
            .tm_mday = 2,
            .tm_hour = 9,
            .tm_min = 30,
            .tm_sec = 0
        }
    };

    dump_student(&st);

    return 0;
 }
