/*
    {
        name: '96 Document Sizes (Bytes)',
        data: [41.67, 14.58, 6.25, 12.5, 9.38, 5.21, 4.17, 3.13, 3.13]
    } (out of 100)
    {
        name: '3443 Image File Sizes (Bytes)',
        data: [16.56, 11.12, 7.75, 38.02, 6.74, 4.53, 6.45, 4.76, 4.07]
    } 
    {
        name: '2597 Image File Sizes (Bytes), Excludes 43 Bytes',
        data: [21.95, 14.75, 10.28, 17.83, 8.93, 6.01, 8.55, 6.31, 5.39]
    }
    
    {
        name: '428 Script File Sizes (Bytes)',
        data: [23.60, 18.46, 14.72, 8.18, 10.75, 6.78, 5.14, 3.97, 8.41]
    }
    
    {
        name: '546 Link File Sizes (Bytes)',
        data: [27.11, 12.09, 9.52, 10.62, 26.74, 4.03, 2.56, 2.01, 5.31]
    }
    [27.235, 14.0625, 9.56, 17.33, 13.4025, 5.1375, 4.58, 3.4675, 5.23]
    Doc count: 96
Link count: 546
Image count: 2597 (3443 with "43" bytes)
Script count: 428
*/

$('#benfords-law-chart').highcharts({
    chart: { },
    title: {
        text: 'Benford\'s Law'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        }        
    ]
});

$('#benfords-law-with-doc-sizes-chart').highcharts({
    chart: { },
    title: {
        text: 'HTML Document Sizes'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        },
        {
            name: 'Leading Digits in Document Size (Bytes)',
            data: [41.67, 14.58, 6.25, 12.5, 9.38, 5.21, 4.17, 3.13, 3.13]
        }   
    ]
});

$('#benfords-law-with-image-sizes-chart').highcharts({
    chart: { },
    title: {
        text: 'Image File Sizes'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        },
        {
            name: 'Leading Digits in Image File Sizes (Bytes)',
            data: [16.56, 11.12, 7.75, 38.02, 6.74, 4.53, 6.45, 4.76, 4.07]
        }  
    ]
});

$('#benfords-law-with-image-sizes-corrected-chart').highcharts({
    chart: { },
    title: {
        text: 'Image File Sizes, Excluding 43 Byte Files'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        },
        {
            name: 'Leading Digits in Image File Sizes (Bytes)',
            data: [21.95, 14.75, 10.28, 17.83, 8.93, 6.01, 8.55, 6.31, 5.39]
        }  
    ]
});

$('#benfords-law-with-link-sizes-chart').highcharts({
    chart: { },
    title: {
        text: 'CSS File Sizes'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        },
        {
            name: 'Leading Digits in CSS File Sizes (Bytes)',
            data: [27.11, 12.09, 9.52, 10.62, 26.74, 4.03, 2.56, 2.01, 5.31]
        }  
    ]
});


$('#benfords-law-with-script-sizes-chart').highcharts({
    chart: { },
    title: {
        text: 'Script File Sizes'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        },
        {
            name: 'Leading Digits in Script File Sizes (Bytes)',
            data: [23.60, 18.46, 14.72, 8.18, 10.75, 6.78, 5.14, 3.97, 8.41]
        }  
    ]
});


$('#benfords-law-with-all-sizes-chart').highcharts({
    chart: { },
    title: {
        text: 'All File Sizes'
    },
    xAxis: {
        categories: ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    },
    yAxis: {
        title: {
            text: 'Frequency'
        }
    },
    series: [
        {
            name: 'Benford\'s Law',
            data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        },
        {
            name: 'Leading Digits in All File Sizes (Bytes)',
            data: [27.23, 14.06, 9.56, 17.33, 13.40, 5.13, 4.58, 3.46, 5.23]
        }  
    ]
});

