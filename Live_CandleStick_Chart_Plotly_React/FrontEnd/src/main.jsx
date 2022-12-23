import React from 'react';
import { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './main.css';
import { options } from './data.js';
import { Select, Spin } from 'antd';
import { newPlot } from 'plotly.js-dist-min';

import axios from 'axios';

// deploy mode dev vs prod config.
// for development
const host = 'http://localhost:80';
// for production
// const host = '';

//globals
var scrip_name = 'Reliance Industries Ltd.';
var ticker = 'RELIANCE.NS';
var period = '1d';
var left_dropdown_value = 'Total Revenue Qtr cr';
var right_dropdown_value = 'Net Profit Qtr Cr';

// global state management using zustand.
// const useBearStore = create((set) => ({
// 	period: '1d',
// 	setPeriod: () =>
// 		set((state) => {
// 			if (state.period === '1d') {
// 				return { period: '2y' };
// 			} else {
// 				return { period: '1d' };
// 			}
// 		}),
// 	doublePopulation: () => set((state) => ({ bears: state.bears * 2 })),
// 	removeAllBears: () => set({ bears: 0 }),
// }));

function App() {
	function mainTickerHandler(_, selected_ticker) {
		scrip_name = selected_ticker['label'];
		ticker = selected_ticker['value'];
		axios
			.get(host + '/ticker', { params: { ticker: ticker, period: period, scrip_name: scrip_name } })
			.then((resp) => {
				let fig_candle = resp.data;
				newPlot('candlestick', fig_candle['data'], fig_candle['layout']);
				document.getElementById('SpinnerCandle').style.display = 'none';
			})
			.catch((e) => console.log('error fetching data from server.', e));

		axios
			.get(host + '/bar', { params: { left_dropdown_value: left_dropdown_value, right_dropdown_value: right_dropdown_value, scrip_name: scrip_name } })
			.then((resp) => {
				let fig_bar = resp.data;
				// console.log(fig_bar);
				newPlot('bargraph', fig_bar['data'], fig_bar['layout']);
				document.getElementById('SpinnerBar').style.display = 'none';
			})
			.catch((e) => console.log('error fetching data from server.', e));
	}

	function TickerDropDown() {
		return (
			<>
				<Select showSearch placeholder='Choose a Scrip.' optionFilterProp='children' onSelect={mainTickerHandler} filterOption={(input, option) => (option?.label ?? '').toLowerCase().includes(input.toLowerCase())} options={options} defaultValue='RELIANCE.NS' />
			</>
		);
	}

	function DurationDropdown() {
		function durationDropdownHandler(selected_period) {
			// console.log(selected_period);
			period = selected_period;
			axios
				.get(host + '/ticker', { params: { ticker: ticker, period: period, scrip_name: scrip_name } })
				.then((resp) => {
					let fig_candle = resp.data;
					newPlot('candlestick', fig_candle['data'], fig_candle['layout']);
				})
				.catch((e) => console.log('error fetching data from server.', e));
		}
		return (
			<>
				<Select
					showSearch
					placeholder='Choose Duration.'
					optionFilterProp='children'
					onSelect={durationDropdownHandler}
					filterOption={(input, option) => (option?.label ?? '').toLowerCase().includes(input.toLowerCase())}
					options={[
						{ label: 'Intraday', value: '1d' },
						{ label: '2 Years', value: '2y' },
					]}
					defaultValue='1d'
				/>
			</>
		);
	}

	function LeftDropdown() {
		function leftDropdownHandler(selected_left_dropdown_value) {
			// console.log(selected_left_dropdown_value);

			left_dropdown_value = selected_left_dropdown_value;
			axios
				.get(host + '/bar', { params: { left_dropdown_value: left_dropdown_value, right_dropdown_value: right_dropdown_value, scrip_name: scrip_name } })
				.then((resp) => {
					let fig_bar = resp.data;
					// console.log(fig_bar);
					newPlot('bargraph', fig_bar['data'], fig_bar['layout']);
				})
				.catch((e) => console.log('error fetching data from server.', e));
		}

		return (
			<>
				<Select
					showSearch
					optionFilterProp='children'
					onSelect={leftDropdownHandler}
					filterOption={(input, option) => (option?.label ?? '').toLowerCase().includes(input.toLowerCase())}
					options={[
						{ label: 'Total Revenue Qtr cr', value: 'Total Revenue Qtr cr' },
						{ label: 'Operating Expenses Qtr Cr', value: 'Operating Expenses Qtr Cr' },
						{ label: 'Operating Profit Qtr Cr', value: 'Operating Profit Qtr Cr' },
						{ label: 'Depreciation Qtr Cr', value: 'Depreciation Qtr Cr' },
						{ label: 'Interest Qtr Cr', value: 'Interest Qtr Cr' },
						{ label: 'Profit Before Tax Qtr Cr', value: 'Profit Before Tax Qtr Cr' },
						{ label: 'Tax Qtr Cr', value: 'Tax Qtr Cr' },
						{ label: 'Net Profit Qtr Cr', value: 'Net Profit Qtr Cr' },
					]}
					defaultValue='Total Revenue Qtr cr'
				></Select>
			</>
		);
	}

	function RightDropdown() {
		function rightDropdownHandler(selected_right_dropdown_value) {
			// console.log(selected_right_dropdown_value);

			right_dropdown_value = selected_right_dropdown_value;
			axios
				.get(host + '/bar', { params: { left_dropdown_value: left_dropdown_value, right_dropdown_value: right_dropdown_value, scrip_name: scrip_name } })
				.then((resp) => {
					let fig_bar = resp.data;
					// console.log(fig_bar);
					newPlot('bargraph', fig_bar['data'], fig_bar['layout']);
				})
				.catch((e) => console.log('error fetching data from server.', e));
		}
		return (
			<>
				<Select
					showSearch
					optionFilterProp='children'
					onSelect={rightDropdownHandler}
					filterOption={(input, option) => (option?.label ?? '').toLowerCase().includes(input.toLowerCase())}
					options={[
						{ label: 'Total Revenue Qtr cr', value: 'Total Revenue Qtr cr' },
						{ label: 'Operating Expenses Qtr Cr', value: 'Operating Expenses Qtr Cr' },
						{ label: 'Operating Profit Qtr Cr', value: 'Operating Profit Qtr Cr' },
						{ label: 'Depreciation Qtr Cr', value: 'Depreciation Qtr Cr' },
						{ label: 'Interest Qtr Cr', value: 'Interest Qtr Cr' },
						{ label: 'Profit Before Tax Qtr Cr', value: 'Profit Before Tax Qtr Cr' },
						{ label: 'Tax Qtr Cr', value: 'Tax Qtr Cr' },
						{ label: 'Net Profit Qtr Cr', value: 'Net Profit Qtr Cr' },
					]}
					defaultValue='Net Profit Qtr Cr'
				></Select>
			</>
		);
	}

	useEffect(() => mainTickerHandler('', { label: 'Reliance Industries Ltd.', value: 'RELIANCE.NS' }));

	return (
		<div className='container'>
			<div className='row'>
				<div className='col-8'>
					<TickerDropDown />
				</div>
				<div className='col-2'>
					<DurationDropdown />
				</div>
			</div>
			<div className='row-fig' id='candlestick'>
				<Spin id='SpinnerCandle' size='large' tip='Please wait.. Fetching data from yFinance api..' />
			</div>
			<div className='row'>
				<div className='col-4'>
					<LeftDropdown />
				</div>
				<div className='col-4'>
					<RightDropdown />
				</div>
			</div>
			<div className='row-fig' id='bargraph'>
				<Spin id='SpinnerBar' size='large' tip='Please wait.. Fetching data from Backend...' />
			</div>
		</div>
	);
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
